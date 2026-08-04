---
title: 如何理解ByteCode、IL、汇编等底层语言与上层语言的对应关系？
date: 2015-01-29
origin: https://www.zhihu.com/question/27831730/answer/38332950
---
# 如何理解ByteCode、IL、汇编等底层语言与上层语言的对应关系？

[知乎链接](https://www.zhihu.com/question/27831730/answer/38332950)

---------

语言的**抽象层次**和其作用以及适用的环境/对象是密切相关的。

那么要理解这些东西与上层语言之间的关系，就要先理解他们存在是为了干什么。
首先，**ByteCode**是VM直接操纵的对象，无论是JIT还是直接解释执行，都是直接跟ByteCode相关。而**上层语言**的源代码则是用于开发者和compiler之间交流的中介，而且更倾向于适应开发者的需要。

如R大 [@RednaxelaFX](https://www.zhihu.com/people/a06cfb38e37dac1658e6457df4d7f032) 所说，Java的字节码本质上是Java AST通过后序遍历的线性序列化形式。
但反过来呢，Java源码相对于ByteCode呢？

MetaInfo而已。
为什么这么说，很重要的一点就是ByteCode是去符号化的。因为VM runtime的任务是**执行指令**和**处理数据**，多出来的东西对它来说都将是累赘。所以除了保存一些跟reflection等特性相关的基本内容在class文件里面，那些本应该被compiler解析和处理的符号都被丢掉了。
而这些被丢掉的信息都可以在源码里面找到，用于辅助调试。否则的话JVM突然抛出来一个NullPointerException，至少要debug半天的ByteCode才能发现是哪儿的问题。

对于机器码和PE文件（*.exe）虽然没像class保存那么多内容，也还是有专门保存符号的symbol file这种东西存在。像 [@vczh](https://www.zhihu.com/people/0970f947b898ecc0ec035f9126dd4e08) 就利用pdb文件实现了C++ reflection这种黑魔法。

而**IL**只是一个相对性的概念，只要不是最顶层和最底层，都可以称为Intermediate Language。
IL的存在是为了分离编译器的前端和后端，同时增强不同语言间的互操作性，我们也可以把Java ByteCode看成一种IL，所有基于JVM的语言都统一编译为ByteCode，再由JVM的JIT编译器进行后期的编译和优化。

那么**汇编语言**也就可以看作在机器码之上引入了符号并且增强了可读性的一种IL。因为所有的变量、过程和计算都变成了对应到stack / register / memory等之上的操作，所以汇编语言里面也就只有那些预定义符号、寄存器名和标号，再进一步翻译成机器码的时候也就变成了数据 / 地址、opcode和偏移量。

也许有用的参考：
[http://yosefk.com/blog/c-as-an-intermediate-language.html](http://yosefk.com/blog/c-as-an-intermediate-language.html)

以上。
