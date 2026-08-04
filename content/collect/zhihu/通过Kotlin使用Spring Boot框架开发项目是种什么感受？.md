---
title: 通过Kotlin使用Spring Boot框架开发项目是种什么感受？
date: 2017-11-23
origin: https://www.zhihu.com/question/68251087/answer/264119853
---
# 通过Kotlin使用Spring Boot框架开发项目是种什么感受？

[知乎链接](https://www.zhihu.com/question/68251087/answer/264119853)

---------

谢[@刘雨培](https://www.zhihu.com/people/60ba2328092904486c9e2fc636ce949d)邀。

Spring本身的设计并没有考虑Kotlin的各种特性，所以用Kotlin写起来跟Java本质上没什么区别。

虽然你可以在其之上再做一层封装，但是这样做跟用任何别的框架或者自己重新造一个的effort差别并不大。

就算gradle说他们有kotlin版本的DSL了，但也都是感觉这是给Android开发人员提供的，非要强行拉到Spring上来用，并不太合适：至少优点没那么明显。
