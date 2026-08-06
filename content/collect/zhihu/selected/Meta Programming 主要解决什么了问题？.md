---
title: Meta Programming 主要解决什么了问题？
date: 2013-08-16
origin: https://www.zhihu.com/question/21486259/answer/18393873
---
# Meta Programming 主要解决什么了问题？

[知乎链接](https://www.zhihu.com/question/21486259/answer/18393873)

---------

Lisp的程序和数据都是基于List，所以只要能够生成list结构，就能相当于能够生成代码，而Lisp的真正强大的宏机制，就是运行时的代码展开与求值。

几乎任何一个稍微大一点的Lisp程序多少都会有一些用来定义宏或者用宏编写的代码。

Ruby的元编程继承自Lisp和Smalltalk，一方面可以通过eval来动态执行代码，另外可以通过构造的语言闭包来打开和关闭作用域。而且有非常简洁和内省/反射机制来对程序的运行时状态判断，进而辅助代码的生成。

C++的模板元编程的作用机制在于编译期，通过模板对类型和数据的计算来进行展开生成代码，所以才会有十分强大和通用的STL（标准模板库）的出现。

Python在某种程度上还是可以进行元编程的（修改元类/数据？），只是灵活程度不够高，所以少有人用，**Python 的哲学态度决定了这个社区会尽量选择远离元编程这东西**。

确切的例子比如Ruby的ActiveRecord，参见[Active Record Query Interface](http://guides.rubyonrails.org/active_record_querying.html)和[rails/activerecord](https://github.com/rails/rails/tree/master/activerecord)。

绝大多数的Ruby DSL都应用了Metaprogramming技巧的，另有书籍：[Ruby元编程](http://book.douban.com/subject/7056800/)。

如果深入研究，元编程的作用还是很大的。抽象能力比之于简单的代码提升了不止一个层级。

> [!info] 2026 年的补充
> 因为很多原因这个过程的界限越来越模糊了。比如前端应用一般都会有预处理编译和打包，Rust程序会加入插件和过程宏，Python的很多框架都混合着decorator，并且可以通过typehint来做进一步的分析和扩展。所以元编程已经融合了太多，对于工具和库作者来说可能还是个明显的概念年，对于应用开发者来说已经没什么必要了。

