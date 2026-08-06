---
title: C++中，为什么函数指针的定义不能将指针类型前置？
date: 2016-08-21
origin: https://www.zhihu.com/question/49606816/answer/118110107
---
# C++中，为什么函数指针的定义不能将指针类型前置？

[知乎链接](https://www.zhihu.com/question/49606816/answer/118110107)

---------

C类型记法跟这个类型的对象声明的时候所在的位置是一致的。

你声明一个函数也是

`int fuck(int);`

所以函数指针应该也是放在 `fuck` 的位置。

`typedef` 也是一样。

你看int i是声明一个变量，所以 `typedef int i` 就是重命名一个类型。

至于 `foreach` 里面，`int(*)(int)` 没有对应的变量，依然能够表示类型啊。

至于为什么 parse 的时候报错，我也不太清楚，试着写个 C++ 前端你应该就能理解了。

就是这样。
