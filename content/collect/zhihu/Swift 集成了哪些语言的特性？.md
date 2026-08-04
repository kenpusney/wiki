---
title: Swift 集成了哪些语言的特性？
date: 2014-06-03
origin: https://www.zhihu.com/question/24007154/answer/26393593
---
# Swift 集成了哪些语言的特性？

[知乎链接](https://www.zhihu.com/question/24007154/answer/26393593)

---------

大部分21世纪静态类型语言必有的东西都被集成了进去，同时附带的还有：
- Generics[泛型] / Type Inference[类型推测]（C++ / Haskell）

- Concepts / Type Constraints[类型约束] （ C# ）

- Algebraic Data Type[代数数据类型] （ Haskell / Rust）

- Closure[闭包] / Anonymous Function[匿名函数] （Objective-C）

- Pattern Matching[模式匹配]（Haskell / Rust）

- Extension[类型扩展] （Ruby / Objective-C / C#）

- Class based Object-Orientation[基于Class的面向对象]（Smalltalk）

- Properties[属性]（C#）

- Protocol based Polymorphism[基于Protocol的多态] （Objective-C）

- Keyword parameters （Objective-C / Python）

如果非要说从谁那里借来的，真的不好下定论，关于Swift的具体设计还要等看过Reference Manual之后才能确定吧。> The Swift language is the product of tireless effort from a team of language experts, documentation gurus, compiler optimization ninjas, and an incredibly important internal dogfooding group who provided feedback to help refine and battle-test ideas. Of course, it also greatly benefited from the experiences hard-won by many other languages in the field, drawing ideas from **Objective-C**, **Rust**, **Haskell**, **Ruby**, **Python**, **C#**, **CLU**, and far too many others to list. （来自：[Chris Lattner's Homepage](http://nondot.org/sabre/)）
