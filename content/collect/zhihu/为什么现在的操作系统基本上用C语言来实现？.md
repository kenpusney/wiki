---
title: 为什么现在的操作系统基本上用C语言来实现？
date: 2015-03-03
origin: https://www.zhihu.com/question/28468921/answer/41026494
---
# 为什么现在的操作系统基本上用C语言来实现？

[知乎链接](https://www.zhihu.com/question/28468921/answer/41026494)

---------

因为只有常接触到的那部分是用C/C++来写的而已。

Pascal，DoD的Ada都是写OS的神器啊。（[System 7](http://en.wikipedia.org/wiki/System_7)）
（说起来我们操作系统课程的教材都是Pascal-like的代码耶！

写一个现代的操作系统的语言至少需要以下特征：
1. 安全。（想想弱类型+无bound check的C语言吧。
2. 高效。
3. 轻量级的运行时依赖或者没有运行时依赖。
4. 有（多）个还算可以的（干）爹。

这样算下来，C++、Rust、去掉GC的D语言这些都是可以的。

当然也可以像[Singularity](http://en.wikipedia.org/wiki/Singularity_%28operating_system%29)那样，直接先用黑魔法搭建一个托管的运行时环境，然后开心的用各种语言写吧。
