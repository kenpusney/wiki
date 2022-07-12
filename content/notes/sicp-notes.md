---
title: SICP 笔记
date: 2020-11-17
---

# 献词

> “我认为，在计算机科学中保持计算中的趣味性是特别重要的事情。这一学科在起步时包含着趣味性。当然，那些付钱的客户们时常觉得受了骗。一段时间之后，我们开始严肃地看待他们的抱怨。我们开始感觉到，自己真的像是要负起成功地、无差错地、完美地使用这些使用这些机器的责任。我不认为我们可以做到这些。我认为我们的责任去拓展这一领域，将其发展到新的方向，并在自己的家里保持趣味性。我希望计算机科学的领域绝不要丧失其趣味意识。**最重要的是，我希望我们不要变成传道士，不要以为你是兜售圣经的人，世界上这种人已经太多了。你所知道的有关计算的东西，其他人也都能学到。**绝不要认为似乎成功计算的钥匙就掌握在你的手里。你所掌握的，也是我认为并希望的，也就是智慧：那种那看到这一机器比你第一次站在它面前时能做得更多的能力，这样你才能将他向前推进。”
> —— Alan J. Perlis

# 序

Programme: 规划

# 第一章 过程抽象

## 1.1 

程序设计的基本元素：

- 表达式
- 命名和环境
- 复合过程
- 过程应用的代换模型（应用序和正则序）
- 条件表达式和谓词

过程作为黑箱抽象。

### 1.1 笔记

第一章的标题是“过程抽象”（Building Abstraction with Procedures），与大家所理解的过程类似，就是由抽象（即函数/过程的定义）和组合组成的结构。

如果连看第一节都能够陷入到细节的坑里去，那这情况可就真的太难了。

其实我有很长一段时间不给人推荐SICP也是出于这个原因。SICP默认使用的是Scheme，这门语言非常容易让人陷入到无穷的细节中去，这些细节拉开来又好像鼓励你去专门了解Scheme(LISP)这门语言一样，导致误入歧途。

我在[:articles/opinion/LISP]()里面也提到了这一点。SICP是本好书，但不一定适合所有人读。也就比如现在的第1.1节，其实就是一块儿非常简单的对Scheme语言的导入，讲什么是表达式，如何绑定变量，如何组合函数调用等等语法层面上的概念，以及特别提了下应用序和正则序这两种求值模型。

我在早期写I2P C++版本的时候，也因入了一章来单独介绍C++的一些初步概念，与这一小节的思路基本上是一致的。

当然这还要看对谁而言。序言中Alan Perlis就说，这本书好就好在用了Scheme，因为他没那么多细节。这里没那么多细节是相对而言的，没有LISP的过度鼓吹的话，Scheme（尤其是这本书所采用的R5RS）确实是一门核心非常小巧的编程语言，专门用于教学、研究和实验用，比起ALGOL的其他方言确实要少了很多细节。但，国内的计算机学子并非第一次接触就是从Scheme开始，当他们带着其他方向的习惯来了解Scheme的时候，会不自觉地代入进去一些自己的想法和理解，而本身很多人学习所带有的目的又有些功利性，这就导致本身想要减少细节来尽可能概括性的讲编程思想的这本书反倒让人容易迷惑。

习题1.5和1.6可以深入看一下，其他的都相对比较基础。

第一节的内容讲了这些基本结构，下一节开始就是去洞悉这些基本结构所组成的“过程”，其运行时的结构是什么样子的。