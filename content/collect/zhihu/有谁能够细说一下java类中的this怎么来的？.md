---
title: 有谁能够细说一下java类中的this怎么来的？
date: 2017-07-10
origin: https://www.zhihu.com/question/56496480/answer/196400904
---
# 有谁能够细说一下java类中的this怎么来的？

[知乎链接](https://www.zhihu.com/question/56496480/answer/196400904)

---------

someObject.nonStaticFuck(shit) => nonStaticFuck_impl(someObject, shit) and internally treat someObject as **this**.
