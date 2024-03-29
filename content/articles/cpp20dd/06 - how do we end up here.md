---
title: 我们是怎么走到这个地步的？
date: 2021-09-01
---

C++23除了是一个即将到来的大补丁以外，还可能将加入另外一个特性，即模式匹配。

当然早在模板出现以后，基于偏特化的模式匹配已经有了。这里会加入的，更多是像类似函数式编程语言中那种基于和类型的模式。

和类型（sum type）这个概念我在另外一个系列文章里面提到过。对于C语言和C++来说，早期要模拟这套操作只能使用tagged union。比如我们解析INI文件或者JSON字段的时候，可能的类型会是字符串、整数或者布尔值。

传统的做法是：
```c++
struct Value {
    union {
        string str;
        int num;
        bool b;
    };
    enum Type { STR, INT, BOOL };
    Type tag;
}
```

当然了，对于有面向对象和动态分发的语言，自然可以换个角度来糊：

```c++
struct Value {};
struct StringValue : Value {
    string str;
};
struct IntValue : Value {
    int num;
};
struct BooleanValue : Value {
    bool b;
};
```

这两种方式本质上并没有什么区别，毕竟都要靠运行时的判断和分发来做些事情。要么一堆的tag判断，要么dynamic_cast，要么就换成用visitor。

不过巧的是某些编程语言的模式匹配实现就是生成一套visitor。

我们之前讲过，C++ 近年来的努力始终都是希望把任何抽象都放到运行时。而和类型与模式匹配这套几乎完全依赖静态类型信息的操作也自然非常适合这样做。于是我们在C++17的时候迎来了std::variant和std::visit。

这一切都起源于C++11的parameter pack，能够让我们在C++ 模板上添加多个参数，于是std::variant就成了这样一个模板：
```C++
template<class... Types>
class variant;

using Value = std::variant<string, int, bool>;

Value strValue = "string value";
Value intValue = 1;
Value boolValue = false;
```

如果是有模式匹配加持的语言，可以预期的操作会是：
```C++
match (value) {
    string s => std::cout << s;
    int s => std::cout << s;
    bool s => std::cout << s;
}
```
可惜这段相当简单的结构在C++里面添加起来实在是非常费劲。虽然C++17也加入了structural binding可以对某些类型进行解构，但远没有达到可以进行模式匹配的地步。如果我们想要做到类似的效果，就只能暂时借用 std::visit。并且需要一个visitor来处理对不同类型的访问。

```C++
struct ValueVisitor {
    void operator()(const string& s) const {
        printf("A string: %s\n", s.c_str());
    }

    void operator()(const int n) const {
        printf("An integer: %d\n", n);
    }

    void operator()(const bool b) const {
        printf("A boolean: %d\n", b);
    }
};

std::visit(ValueVisitor(), value);
```

尽管这样做仍然是静态分发的，但看起来就太复杂了。如果我们有更方便的方式来构建visitor，可能会更好一点。而lambda表达式作为可以静态分发的工具自然非常方便我们来达成对应的效果。预期的场景可能像下面这样：

```c++
make_visitor(
    [](const string& s) {
        printf("string: %s\n", s.c_str());
    },
    [](const int d) {
        printf("integer: %d\n", d);
    },
    [](const bool b) {
        printf("bool: %d\n", b);
    }
)
```

前面提到了 C++11 有了parameter pack，可以帮我们变着法的组合出来这套操作。

```c++
template <class... Fs>
struct overload;

template <class F0, class... Frest>
struct overload<F0, Frest...> : F0, overload<Frest...>
{
    overload(F0 f0, Frest... rest) : F0(f0), overload<Frest...>(rest...) {}

    using F0::operator();
    using overload<Frest...>::operator();
};

template <class F0>
struct overload<F0> : F0
{
    overload(F0 f0) : F0(f0) {}

    using F0::operator();
};

template <class... Fs>
auto make_visitor(Fs... fs)
{
    return overload<Fs...>(fs...);
}
```

这里利用了C++模板偏特化的一个老传统，必须进行类似的递归定义才行。每一个overload模板展开其实都相当于包裹了对应位置的lambda表达式，并且继承了其 `operator()`。而每一个overload模板又是比其少一个参数的overload模板的子类，也继承了父类的 `operator()`。这样套娃下来，就达成了我们想要的结果。

然而在C++17的时候，parameter pack被扩展到了 fold 表达式和 using 声明中，于是就不再需要递归地糊这一堆递归了。同时C++17引入了CTAD（类模板参数推导），可以使用deduction guide来代替笨拙的make_visitor函数。

```c++
template<class... Ts> struct overloaded : Ts... { using Ts::operator()...; };
template<class... Ts> overloaded(Ts...) -> overloaded<Ts...>;
```

C++20中扩展了CTAD的规则，以至于连最后那行deduction guide也可以直接省略掉。

于是我们的visit就可以写成：
```c++
std::visit(overloaded {
    [](const int& ) { /* ... */ },
    // ...
}, value);
```

虽然还是丑了点，但这相较于需要改动编译器引入新的语句和结构来实现的模式匹配来说，已经是相当轻量而且方便了。更关键的是，从parameter pack，到CTAD，到lambda表达式，都并非为了sum type 和模式匹配而准备的，但这些有机地组合在了一起就让C++能够实现堪比函数式编程语言的表达能力，并且因为完全是编译时的操作，完全不会带来运行时负担和额外的性能开销。

不过相应的问题就是要去了解那么多`...`所表示的意思以及复杂的deduction guide规则了。对于库使用者相对来说还不是那么必要，但是库作者需要对外提供更加友好的接口和DSL的时候，就需要充分了解相关的内容。

后续的文章我们会看一下C++其他的关于模式匹配的设计，以及现阶段的模式匹配的Proposal。