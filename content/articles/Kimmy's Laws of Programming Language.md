---
title: Kimmy 编程语言定律
date: 2014-11-22
---

## 第一定律（领域特定原则）

初始版本：

> 当且一个拥有静态类型的编程语言实现了内置（built-in）的关联集合（Map）和关联集合字面量（map literal）时，这个语言就无法再用作写操作系统（编译器、数据库系统等等）。

其他表述：

> 一切编程语言都是面向特定领域（Domain-Specific）的。
> （见[《如何设计编程语言》]({{< relref "/articles/htdpl/01. How To Design Programming Language.md" >}})

示例：
- Go

## 第二定律（可用性定律）

初始版本：

> 只有当一个编程语言/平台有了对应的xUnit框架，这个平台才能做到Production Ready。

该定律有一系列的推论，比如：

  1. 编程语言可用性：直到这个编程语言在没有xUnit框架之前，是不足以用于生产系统的。
  2. xUnit框架必要性：任何一个编程语言要想用于生产系统，就必须设计并提供一套可用的xUnit框架。