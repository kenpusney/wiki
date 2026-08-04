---
title: 哪一种计算机语言最适合入门？是C语言吗？可是我觉得指针难死了！？
date: 2015-11-26
origin: https://www.zhihu.com/question/37818126/answer/74048418
---
# 哪一种计算机语言最适合入门？是C语言吗？可是我觉得指针难死了！？

[知乎链接](https://www.zhihu.com/question/37818126/answer/74048418)

---------

讲真，这样的话我只能告诉你，适合新手的编程语言是OCaml。

它里面的**ref**让你很直观的就能理解了。前提是你能理解前面所有的东西。
```ocaml
type 'a ref = { mutable contents: 'a };;

let ref x = { contents: x };;    (*  &x      *)
let (!) r = r.contents;;         (*  *r      *)
let (:=) r x = r.contents <- x;; (*  *r = x  *) 
```

===================================
指针都觉得难。

那
```cpp
T&
T&&
const T*
T* const
const T&
const T&&
std::shared_ptr<T>
std::weak_ptr<T>
std::unique_ptr<T>
std::experimental::observer_ptr<T>
boost::instructive_ptr<T>

```

以及
```cpp
T^
cli::pin_ptr<T>
cli::interior_ptr<T>

```

是不是感到很绝望？

如果你觉得Linux代码很难读懂，来我们一起看Boost代码吧。

=================统一解答评论分割线====================

> 1. 这些东西都比“指针”简单。


好的，请解释以下基本概念：
- 垃圾回收

- 右值/右值引用

- 所有权

- 移动

- borrow（鉴于还没有统一的中文翻译，只好这样写）

- 引用计数

- 循环引用

以及
- 代理对象（Proxy）


> 2. 题主问的是简单的适合入门的编程语言。我回答的不合题意。


但是请你们看题目具体的描述，谢谢。

> 3. Linux并不比Boost简单


废话，一个发展了二十多年的操作系统内核，肯定有很多积累，要说它简单绝对不可能。
但是，Linux本身复杂的原因并不在于C语言，而是由操作系统这样一个系统软件自身决定的。更何况Linux这种没事儿谁都可以插一脚的项目。所以，Linux的难度在于资源管理、调度和各种优化的实现，而不是“指针”怎么用。同样地你也可以看看[xnu](https://github.com/opensource-apple/xnu)和[WRK](https://github.com/hacksysteam/WRK-1.2)。
然而你再看Boost在做什么事？
扩展C++。

> 4. 这说明C++太复杂了


并不是这个意思。只是反讽一下题主，自己（和选择的教材/导师）水，反而怪C语言，就像拉不出屎怪地球引力小一样。

另外，C++也是一门新手友好的语言。当然主要看你学的是哪一方面。
[C++: From Novice to Professional](http://www.douban.com/doulist/4041785/)

> 5. 懂这就很牛逼吗？


当然不是。但是连1中我提到的超过一半的概念都不懂的话，还是不要随便评论了吧。

> 6. C++不适合时代了，大家宁可用C也不用这个


[GCC's move to C++ [LWN.net]](https://lwn.net/Articles/542457/)

> 7. 然后呢？


并没有然后。不想看就折叠我吧。

> 8. T^是什么？


[C++/CLI](https://en.wikipedia.org/wiki/C%2B%2B/CLI)
