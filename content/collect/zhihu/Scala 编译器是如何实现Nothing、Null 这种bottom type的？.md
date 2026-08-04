---
title: Scala 编译器是如何实现Nothing、Null 这种bottom type的？
date: 2015-12-13
origin: https://www.zhihu.com/question/38476197/answer/76616598
---
# Scala 编译器是如何实现Nothing、Null 这种bottom type的？

[知乎链接](https://www.zhihu.com/question/38476197/answer/76616598)

---------

```text
typedef decltype(nullptr) nullptr_t;

```
