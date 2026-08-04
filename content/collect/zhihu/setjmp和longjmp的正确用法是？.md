---
title: setjmp和longjmp的正确用法是？
date: 2014-11-04
origin: https://www.zhihu.com/question/26480396/answer/32928361
---
# setjmp和longjmp的正确用法是？

[知乎链接](https://www.zhihu.com/question/26480396/answer/32928361)

---------

> 这两个函数通常用于异常处理吗，正确的使用姿势是？

这两个函数就是拿来做跳转用的，不止是异常处理。甚至可以直接拿来搞[Coroutine](http://yosefk.com/blog/coroutines-in-one-page-of-c.html)。
正确的用法就是不要轻易用它。或者，至少做一个像样的[封装](http://www.di.unipi.it/~nids/docs/longjump_try_trow_catch.html)。> 和return error_code相比有什么优势？

和大多数API直接提供的return error_no对比，基本上没有什么优势（当然还是要看风格的）。
