---
title: Swift 集成了哪些语言的特性？
date: 2014-06-03
origin: https://www.zhihu.com/question/24007154/answer/26393593
---
# Swift 集成了哪些语言的特性？

[知乎链接](https://www.zhihu.com/question/24007154/answer/26393593)

---------

大部分21世纪静态类型语言必有的东西都被集成了进去，同时附带的还有：
- Generics / Type Inference（C++ / Haskell）
- Concepts / Type Constraints （ C# ）
- Algebraic Data Type （ Haskell / Rust）
- Closure / Anonymous Function（Objective-C）
- Pattern Matching（Haskell / Rust）
- Extension （Ruby / Objective-C / C#）
- Class based Object-Orientation（Smalltalk）
- Properties（C#）
- Protocol based Polymorphism（Objective-C）
- Keyword parameters （Objective-C / Python）

如果非要说从谁那里借来的，真的不好下定论，关于Swift的具体设计还要等看过Reference Manual之后才能确定吧。

> The Swift language is the product of tireless effort from a team of language experts, documentation gurus, compiler optimization ninjas, and an incredibly important internal dogfooding group who provided feedback to help refine and battle-test ideas. Of course, it also greatly benefited from the experiences hard-won by many other languages in the field, drawing ideas from **Objective-C**, **Rust**, **Haskell**, **Ruby**, **Python**, **C#**, **CLU**, and far too many others to list. （来自：[Chris Lattner's Homepage](http://nondot.org/sabre/)）
