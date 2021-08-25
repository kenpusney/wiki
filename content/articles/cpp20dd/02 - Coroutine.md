---
title: Coroutine
---

我们来看另外一个语言特性的改动，coroutine。

开始之前先说一下C++这十几年的方向。因为一个zero-runtime overhead的承诺，C++基本上放弃了在运行时解决问题的这条路，主要的改动都是在尝试增强编译时。除了C++11 引入了线程以后对内存模型有了较大的改动以外，几乎没再怎么糊过运行时的东西。因为太难了：要考虑target到那么多个平台，各家都存在不同的问题，连ABI至今都没办法有个基本的解决方案的情况下往里面越挖反而问题越多。

于是，coroutine这个直接影响运行时行为的东西怎么解决的呢？

C++的方案是，放到编译时来搞。

于是C++20的coroutine拿到手并不能直接用，因为C++只是给你定义了一套结构和规范，并且如果你正确实现了这套规范以后才可能享受到coroutine提供的便利。不是不想要runtime overhead嘛，我不提供runtime就好了，你自己实现。

单纯来看，C++中的coroutine就是一个包含了`co_yield`、`co_return`或者`co_await`的函数。但是C++编译器会把他转化成一个特定的结构。这个结构会创建一个coroutine状态对象，然后根据编译器解析生成的代码配合用户选择的返回对象（return object）来执行。

听起来好像什么都没说，我们直接看一个例子：

```c++
generator<int> range(int from, int to) {
  for (int x = from; x < to; ++x) {
    co_yield x;
  }
}
```

看起来似乎很简单，并没有说的那么夸张。但实际上，至少在目前的标准中你是没有`generator<T>`这个模版类可以直接拿来用的，需要自己糊出来。大概是这个样子：

```C++
template<class T>
struct generator {
  struct promise_type;
  using handle = std::coroutine_handle<promise_type>;

  struct promise_type {
    std::optional<T> current_value;

    auto get_return_object() { return generator{handle::from_promise(*this)}; }
    auto initial_suspend() noexcept { return std::suspend_always{}; }
    auto final_suspend() noexcept { return std::suspend_always{}; }
    void unhandled_exception() { std::terminate(); }
    auto yield_value(T value) {
      current_value = std::move(value);
      return std::suspend_always{};
    }
  };
  ...

```

关键的部分就是这个`promise_type`：coroutine里面的各种步骤都会映射到上面的所有方法上面。整个的coroutine执行过程大概是下面这个样子：

```C++
{
  co_await promise.initial_suspend();
  try
  {
    <body-statements>
  }
  catch (...)
  {
    promise.unhandled_exception();
  }
FinalSuspend:
  co_await promise.final_suspend();
}
```

而其中的任何`co_yield`和`co_return`也都会翻译成对应的语句：

```c++
co_await promise.yield_value(a);  // `co_yield a`
co_await promise.return_value(a); // `co_return a`
co_await promise.return_void();   // `co_return`
```

这样配合着实现`generator`的`iterator`，就能够顺利地在C++中实现Python或者JavaScript中类似的Generator了。

```C++
// pesudo code
template<class T>
struct generator {
  ...
  struct iterator {
    void operator++() { ... }
    T& operator*() { ... }
  };

  iterator begin() { ... }
  iterator end() { ... }
  ...
```

上面定义的range协程使用起来也非常简单：
```C++
for (auto&& i : range(0, 10)) {
  std::cout << i * i << std::endl;
}
```
前面定义的`iterator`和`begin`/`end`就是为了这里的range-based for语法。

好的我们再从头解释一下coroutine的执行过程：

- 首先，定义一个coroutine，需要一个return object。编译器会根据这个return object找到对应的`promise_type`。同时根据这个coroutine生成一个创建状态对象的结构。这个状态对象包含了coroutine的参数和一些必要的执行环境。
- coroutine运行的时候，会初始化coroutine状态对象，然后创建promise对象。并且根据这个promise获取coroutine的返回对象（`promise_type::get_return_object()`）。然后根据`initial_suspened()`做一些初始化操作。
- 所有的`co_return`、`co_yield` 或者 `co_await` 都会对应到一个awaitable object，来决定当前协程的挂起状态，并且做一些写回或者唤醒操作。
- 而在return object里，可以拿到当前的coroutine的promise对象，然后再对其行为进行控制。比如唤醒或者获取写回的值等。比如适配上iterator traits就能直接利用STL和Ranges了。
- 等到coroutine执行结束，会调用`final_suspend()`来做一些清理工作。

整个过程不会有什么额外的运行时负担，都会在编译期生成好，而调度工作也是用户来控制的，所以你完全可以利用这套规则来设计各种自定义的控制流。

到这里问题又来了。如果每实现一个类似的coroutine运行时都要来这么一套，那怎么给一些已存在的结构添加上`promise_type`呢。

早在C++0x时代大家就预想到了这个问题，比如如果一个定义的约束无法被满足，可以使用一些特化手段给他加上。对应的约束就是concept，而这套特化手段就是concept map。不过在Concept TS中已经被阉割到了只剩下约束了，而且`promise_type`是没有明确定义的标准concept可以拿来用，所以concept map是指望不上了。

不过在这之前仍然还有一个上古神器，就是type traits。如果一套约束是按照type traits的思路来设计的，是很容易给已有类型添加额外的特性的。前面提到的iterator traits就是如此。C++也在标准库里提供了`std::coroutine_traits`。

比如，对于C++标准库的`std::future`类型，我们可以直接扩展到coroutine上，利用`std::promise`作为`promise_type`。
```C++
template <typename T, typename... Args>
requires(!std::is_void_v<T> && !std::is_reference_v<T>)
struct std::coroutine_traits<std::future<T>, Args...> {
  struct promise_type : std::promise<T> {
    std::future<T> get_return_object() noexcept {
      return this->get_future();
    }

    std::suspend_never initial_suspend() const noexcept { return {}; }
    std::suspend_never final_suspend() const noexcept { return {}; }

    void return_value(const T &value)
    noexcept(std::is_nothrow_copy_constructible_v<T>) {
      this->set_value(value);
    }
    void return_value(T &&value)
    noexcept(std::is_nothrow_move_constructible_v<T>) {
      this->set_value(std::move(value));
    }
    void unhandled_exception() noexcept {
      this->set_exception(std::current_exception());
    }
  };
};
```

同时重载`co_await`运算符，来让future可以组合：
```C++
template <typename T>
auto operator co_await(std::future<T> future) noexcept
requires(!std::is_reference_v<T>) {
  struct awaiter : std::future<T> {
    bool await_ready() const noexcept {
      using namespace std::chrono_literals;
      return this->wait_for(0s) != std::future_status::timeout;
    }
    void await_suspend(std::coroutine_handle<> cont) const {
      std::thread([this, cont] {
        this->wait();
        cont();
      }).detach();
    }
    T await_resume() { return this->get(); }
  };
  return awaiter{std::move(future)};
}
```

这样你就成功拥有了别的语言里费尽心思糊进去的`async`和`await`：

```C++
std::future<int> compute() {
  int a = co_await std::async([] { return 6; });
  int b = co_await std::async([] { return 7; });
  co_return a * b;
}
```

另外，如果你还是觉得太麻烦，可以先忍一忍。等到C++23，大概就能用上标准化的std::generator和std::task了。
