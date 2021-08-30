---
title: Ranges
---

我们看C++20中三大特性中的第四个，ranges。

早在二十几年前的C++ STL中就已经有相应的概念，即iterator（迭代器）。C++ 的iterator与普通语言中的迭代器有所不同，比如Java，iterator只需要满足非常简单的接口就好了：

```java
interface Iterator<E> {
  boolean hasNext();
  E next();
}
```

这种迭代器有一个非常不友好的问题就是，只能进行前向迭代，拿下一个元素。但是对于数组（包括std::array）或者std::vector这种连续性容器来说，更多的时候我们需要非常频繁的随机访问，而对于双链表则更有可能从后向前迭代或者前后折腾。当仅有如Java的Iterator这种简单的抽象的时候，并不能设计一些通用的接口。比如排序，对于不同特性的容器，所需要的排序操作就必然有所不同。

Java解决问题的方式是提供了Arrays.sort和Collections.sort两个静态方法。但在C++ 的泛型能力下，使用统一的接口来做静态分发，完全可以做到比Java更优雅。

于是就有了iterator category这个概念。对于不同类型的容器（包括裸指针T*），都有对应的分类，分别是：

- input_iterator 用于读取数据的迭代器
- output_iterator 用于写入数据的迭代器
- forward_iterator 前向迭代，约束比input iterator更强的迭代器
- bidirectional_iterator 可双向迭代的迭代器
- random_access_iterator 可随机访问的迭代器

以及C++17中加入的：

- contiguous_iterator 元素在逻辑顺序和物理顺序上都是连续的迭代器

前面提到了，有了iterator category的一个好处就是可以直接按照迭代器的相关特性来分发功能。比如std::sort的要求就是必须满足可随机访问的迭代器才能进行排序，但相对宽松的std::copy，只要求提供input iterator来作为复制的源以及output iterator作为复制的目标就能进行复制操作了。

于是我们可以非常简单的在C++ 里实现一个cat程序：
```c++
std::copy(
  std::istreambuf_iterator<char>(std::cin),
  std::istreambuf_iterator<char>(),
  std::ostreambuf_iterator<char>(std::cout));
```

能这样做的一个原因就是我们给输入流和输出流都实现了迭代器，进而可以利用各种标准库算法。

但是这里就有了一个诡异的问题，于是产生了后来的ranges提案。

我们看上面那个copy，其对应的签名如下：
```c++
template<class InputIterator, class OutputIterator>
OutputIterator copy(
  InputIterator first,
  InputIterator last,
  OutputIterator dest
);
```

看到问题了吧，大部分情况下，iterator在使用的时候必须以first/last的形式成对出现，算法所作用的是一个前闭后开的`[first, last)`区间。这样一来很多算法就只能做成inplace的，而且没办法做一些相对简单的组合。

比如你想做一套流式编程里的map reduce，在C++ 里只能先transform，再accumulate。

```c++
#include <ranges>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <vector>

template<class Collection>
template<class Collection>
auto map_reduce(const Collection& c, auto fn, auto init, auto acc) {
  std::vector<typename Collection::value_type> transformed {};
  std::transform(
    c.begin(), 
    c.end(), 
    std::back_inserter(transformed), 
    fn);
  return std::accumulate(
    transformed.begin(), 
    transformed.end(), 
    init, acc);
}
```

那么既然`[begin, end)`表示一个范围区间，直接用一个统一的range对象表示不就好了吗。

于是我们就迎来了Ranges提案，并在C++20中合并进了标准库。

一个range非常简单，有 begin 和 end 就行了。
```c++
template<class T>
concept range = requires(T& t) {
  ranges::begin(t);
  ranges::end(t);
};
```

同样在这基础之上，也有与iterator category对应的range concept，满足了对应concept的range自然也能够做针对性的静态分发。

有了range以后我们就能换种方式来设计前面的 map_reduce 函数：
```c++
template<std::ranges::range Range>
auto map_reduce_range(const Range& r, 
  auto fn, auto init, auto acc) {
  auto transformed = r | std::views::transform(fn);
  return std::reduce(
    transformed.begin(), 
    transformed.end(), 
    init, acc);
}
```

这样除了简化了靠begin/end传递的iterator的麻烦，让对应的操作可以组合以外，还附带了额外的优化点。

在最初的 map_reduce 函数里，为了保留 transform 的中间结果，我们不得不创建一个临时的vector对象，然后再对其accumulate。而在Ranges提案里引入了view的概念，即一个没有所有权的代理对象。view也是一种range，但是相对于传统的容器来说，并不会实际持有内部的元素，只有在获取其元素的时候才进行求值。

比如在 map_reduce_range 函数里，transformed 对象就是一个由range和transform_view组合而成的view，除了持有range r的迭代器以外，并不会有任何额外的内存分配，也不会进行实际的transform操作。当reduce操作进行规约运算的时候才会进行具体的transform变换（即调用fn函数）。

这个时候你大概可以把view看成是Java里的Stream。

当然了，跟Steam必须先有流才能操作不一样，C++ 还允许你做一些别的事情。

前面你应该注意到了，我们在 map_reduce_range 函数里面实际使用额并不是transform_view，而是std::ranges::transform，后者其实是一个适配器，用来把range转换成transformed_view。transform有两种调用方式：

- transform(range, fn) 直接适配到特定的对象，转换成一个transform_view
- transform(fn) 部分应用适配器，生成一个range适配器闭包对象，用于通过管线操作符 `|` 进行组合操作。

任何适配器都可以使用这两种方式调用。同时，多个适配器闭包对象可以进行组合，即，对于一个包含了range R和适配器闭包C、D的管线操作：

- `R | C | D` （按照优先级和结合性，即 `(R | C) | D`）

其等同于：

- `R | (C | D)`

因此你完全可以先把某几个适配器闭包组合起来，然后在任何方便的时候在应用到特定的range上。

```c++
auto doubles_odd = 
    views::filter([](auto x) { return x % 2 != 0; }) 
  | views::take(5)
  | views::transform([](auto x) { return x * 2; });

auto doubled_odds = views::iota(1) | doubles_odd;
```

这里 iota 生成了一个从 1 开始的无穷整数序列，doubles_odd 则筛选其中的奇数，然后取前 5 个，再对其中的每一个数 * 2。这样下来整个风格就更贴紧函数式风格了，而且因为C++ 本身的设计，又不会带来明显的运行时负担。

但同前面几个特性一样，C++20的range也有些许遗憾。虽然是少有的直接集成了concept的库，其中可以直接使用的adaptor并不多，很多东西则需要通过ranges-v3库中view来补充。不过好在ranges补完计划也已经提到C++23议程里面去了，就等这个补丁版本发布看能否有更好的进展吧。
