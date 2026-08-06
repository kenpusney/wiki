---
title: 为什么 C/C++ 的宏一直没怎么发展？
date: 2014-03-08
origin: https://www.zhihu.com/question/22952377/answer/23216362
---
# 为什么 C/C++ 的宏一直没怎么发展？

[知乎链接](https://www.zhihu.com/question/22952377/answer/23216362)

---------

C++中的预定义宏和条件编译宏只是简单的在编译期前进行预编译文本替换，整体的能力如同m4。

某种程度上可以作为生成代码的工具，但局限性太大。特别是call-by-name这一点。。针对这一点， [@vczh](https://www.zhihu.com/people/0970f947b898ecc0ec035f9126dd4e08)曾设计过FPMacro来避免和增强，参见[如何设计一门语言（十）——正则表达式与领域特定语言（DSL）](http://www.cppblog.com/vczh/archive/2013/09/16/203249.html)中相关内容。

至于为什么本身没有发展，很大的一点是考虑兼容性的问题。

不过同样与Lisp的强大的宏有一个相对的东西，在C++中也是非常重要的组成部分的，就是C++中的[模板 (C++)](http://zh.wikipedia.org/zh-cn/%E6%A8%A1%E6%9D%BF_(C%2B%2B))：编译时进行展开生成可用代码。同时，对于类型推断和一些简单的值运算也能做到在编译期完成，通过这些精妙的设计带来的效果不比Lisp的宏系统少。（当然在美观性和友好性方面就不要多说了，C++程序员的内伤。

如同 [@白如冰](https://www.zhihu.com/people/9558cac1a967147f0318fe6b7b1a0f7b)一样，推荐你去了解一下boost，特别是 `boost::mpl`。

另推荐参考：
- [Template metaprogramming](http://en.wikipedia.org/wiki/Template_metaprogramming)
- [C++Templates中文版 (豆瓣)](http://book.douban.com/subject/2378124/)
- [C++模板元编程 (豆瓣)](http://book.douban.com/subject/4136223/)
- [C++设计新思维 (豆瓣)](http://book.douban.com/subject/1119904/)

另贴一个很明显的利用模版做出来的东西，by [@vczh](https://www.zhihu.com/people/0970f947b898ecc0ec035f9126dd4e08)
[https://gist.github.com/kenpusney/9274727](https://gist.github.com/kenpusney/9274727)
