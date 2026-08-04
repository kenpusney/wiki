---
title: 为什么 constexpr 没有被作为类型的一部分？
date: 2018-11-17
origin: https://www.zhihu.com/question/302742670/answer/533514403
---
# 为什么 constexpr 没有被作为类型的一部分？

[知乎链接](https://www.zhihu.com/question/302742670/answer/533514403)

---------

因为那样只会让类型系统更复杂吧。

constexpr 还是只做一个告诉编译器这里有可能直接做编译时计算的标志就好了。
