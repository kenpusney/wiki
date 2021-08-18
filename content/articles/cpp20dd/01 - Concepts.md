---
title: Concepts
draft: true
date: 2021-08-12
---

我们先从整个 C++ 社区心念多年的特性说起。

首先我们来看 Concept 是什么。

[泛型编程](https://mp.weixin.qq.com/s/F-_vBBgOSMGtz21O66NyBQ)中，我们通常需要限制某个类型的行为，并通过这种方式来保证我们使用泛型的代码是正确的，不存在异常行为。

比如 Java 提供了泛型约束的方式，如果你没有在泛型参数列表中声明某类型需要满足的约束，那就只能把该类型的对象当成 `Object` 来用，或者使用 `instanceof` 和强制类型转换来得到你想要的方法。

这样的结果就是，[是否使用泛型根本没啥区别](https://mp.weixin.qq.com/s/E2rfuPvIpUTP2qOHNS40-w)。

比如我们需要处理一个可迭代对象：

```java
class Processor<T extends Iterable<?>> {
  void process(T t) {
    t.iterator() // !
  }
}
```

备注了 `!` 的那行代码就通过我们在类型声明处的 `extends Iterable<?>` 约束来保证的。这样就不会出现编译期的类型异常。

不过这个操作其实也有很多问题。

- 首先是你得定义一个 interface 来做约束，这样运行时的时候也必须带上这个符号，没办法消除。
- 其次，对应所限制的类型必须实现这个 interface，这样不能对已存在的类型做限制（除非使用动态代理），而对于可以控制和修改的类型，也不得不引入额外的虚方法调用来增加这个运行时负担
- 另外，这种方式限制了约束的内容，接口中不能声明的部分，比如构造方法，则没办法进行约束。

而远在 Concept 还没进入标准之前，C++就已经能做到类似的操作了，只是过程有些复杂。

比如，我们要限制一个类型参数必须是可以默认构造的（即有一个公开的无参构造函数），要怎么做呢？

（以下代码是简化版，没有进行 `remove_cv` 或者 `decay` 的处理）

```c++
// 1
template<class T, class U = std::void_t<>>
struct IsDefaultConstructible: std::false_type {};

// 2
template<class T>
struct IsDefaultConstructible<T, std::void_t<decltype(T())>>: std::true_type {};

// 3
struct T {};
struct U { U(int) {}; };

// 4
static_assert(IsDefaultConstructible<T>::value == true);
static_assert(IsDefaultConstructible<U>::value == false);

// 5
template<class T, std::enable_if_t<IsDefaultConstructible<T>::value>* = nullptr>
struct RequiresDefaultConstructible {
  T x = T {};
};

// 6
RequiresDefaultConstructible<T> {};

// 7
RequiresDefaultConstructible<U> {};
```

这段代码会在`// 7`处编译失败，因为 U 只有一个带参构造函数，无法进行无参构造。

我们来分别解释一下这些代码干了啥

- `// 1`处我们声明了一个 IsConstructible 的 type traits，默认所有结果都为 false。
- `// 2`处，我们使用 decltype 对可默认构造的类型进行了特化，特化的结果是 true。
- `// 3`处，我们定义了两个类型 T 和 U，分别为可默认构造和不可默认构造。
- `// 4`处我们进行了验证，确认编译期的这个 type traits 工作正常。
- `// 5`我们定义了一个使用到了该 type traits 的模版，通过 SFINAE 来在编译时保证所有的参数 T 都是可默认构造的。
- `// 6`和`// 7`处我们实例化这个模版，第一个当然是 OK 的，因为 T 可默认构造，第二个则因为编译时的类型替换出问题导致编译失败。

上面的操作充斥着 C++ 元编程技巧，远比声明一个接口就使用要复杂得多；并且熟悉的朋友应该已经看出来了，`decltype` 是 C++11 的，`enable_if_t` 是 C++14 的，`void_t` 是 C++17 的，在这些特性和工具库未出现之前的 C++03，想要实现就要更复杂很多。

并且，糟糕的是，即便在 2021 年的 gcc 11 编译器上，`// 7`行的编译错误信息都几乎跟 `IsConstructible` 毫无关系：

```text
In substitution of 'template<bool _Cond, class _Tp> using enable_if_t = typename std::enable_if::type [with bool _Cond = false; _Tp = void]':
test.cpp:23:35:   required from here
error: no type named 'type' in 'struct std::enable_if<false, void>'
 2514 |     using enable_if_t = typename enable_if<_Cond, _Tp>::type;
      |           ^~~~~~~~~~~
test.cpp: In function 'int main()':
test.cpp:23:35: note: invalid template non-type parameter
   23 |     RequiresDefaultConstructible<U> {};
      |                                   ^
```

每一个调试 C++ 模版的人上辈子都是折翼的天使。

终于千呼万唤始出来的 Concept，解决了大部分相关的问题。在有了 Concept 的情况下，限制默认构造可以这样写了：

```c++
template<class T>
concept DefaultConstructible = requires {
    T {};
};

template<DefaultConstructible T>
struct RequiresDefaultConstructible {
    T x = T {};
};
```

这个时候当你再去实例化 `RequiresDefaultConstructible<U>`，一切都变得那么简单自然：

```text
test.cpp:20:35: error: template constraint failure for 'template<class T>  requires  DefaultConstructible<T> struct RequiresDefaultConstructible'
   20 |     RequiresDefaultConstructible<U> {};
      |                                   ^
test.cpp:20:35: note: constraints not satisfied
test.cpp: In substitution of 'template<class T>  requires  DefaultConstructible<T> struct RequiresDefaultConstructible [with T = U]':
test.cpp:20:35:   required from here
test.cpp:5:9:   required for the satisfaction of 'DefaultConstructible<T>' [with T = U]
test.cpp:5:32:   in requirements  [with T = U]
test.cpp:6:5: note: the required expression 'T{}' is invalid
    6 |     T {};
      |     ^~~~
```

更重要的是，Concept 的验证和模版的展开完全是编译期的，`requires` 块里你可以写各种可能的验证，并且 Concept 本身就是个 `bool` 类型的结果，所以可以结合之前几乎所有的 C++ type traits 一起用。

即便是拖了这么久才实现出来，这项特性依然是能够吊打绝大多数编程语言的泛型约束功能。

至于 Concept 这项功能到底有什么用呢？我们到后面讲到 Ranges 的时候再细说。
