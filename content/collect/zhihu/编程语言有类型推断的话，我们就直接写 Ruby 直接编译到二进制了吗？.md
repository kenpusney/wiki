---
title: 编程语言有类型推断的话，我们就直接写 Ruby 直接编译到二进制了吗？
date: 2014-01-01
origin: https://www.zhihu.com/question/22399630/answer/21292732
---
# 编程语言有类型推断的话，我们就直接写 Ruby 直接编译到二进制了吗？

[知乎链接](https://www.zhihu.com/question/22399630/answer/21292732)

---------

要看你说的二进制代码是指Native Code还是Bytecode
把Ruby编译为Native代码必然还是要一定的约束才行。
最重要的就是要在编译期确定其类型（显式声明也好，类型推断也好），否则必然不能够脱离一个运行时环境。
如果说说编译为Bytecode，当然现在的Ruby实现也有，也是要依赖一个运行时环境（YARV / LLVM 啥的）。PyPy的做法也是如此。
同样，许多高级一些的系统编程语言也是需要依赖一定的运行时（因为GC之类高级特性），比如Go和D语言，虽然两者都是静态类型，都是显式的编译为Native文件。

Crystal的做法应该没有脱离上面几种情况。

至于类型推断的好处，一方面可以简化显式类型声明带来的一些多余的操作（虽然很多时候这些东西是很有必要的），另一方面，又不会失却静态类型和强类型的安全性和高效，所以这基本是一个追求效率的语言现常常采取的做法。

参考：
[Type inference](http://en.wikipedia.org/wiki/Type_inference)
[类型和程序设计语言 (豆瓣)](http://book.douban.com/subject/1318672/)
