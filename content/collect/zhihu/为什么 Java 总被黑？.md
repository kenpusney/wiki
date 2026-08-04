---
title: 为什么 Java 总被黑？
date: 2015-10-27
origin: https://www.zhihu.com/question/36899399/answer/69517112
---
# 为什么 Java 总被黑？

[知乎链接](https://www.zhihu.com/question/36899399/answer/69517112)

---------

谢邀。

一不小心给LYP [@刘雨培](https://www.zhihu.com/people/60ba2328092904486c9e2fc636ce949d) 菊苣点了反对，另外也刚好我是唯一一个被折叠的回答，改正一下看能不能再冒个泡。

楼上抖机灵的太多了，打偏了的也太多了，所以我也只能再妄自回答一下了。

Java语言：
最大的问题就是Checked Exception。
其次是语法太verbose（可以用Groovy等来解决这个问题，
至于API设计的问题，更多的原因还是来自第一条。引入Stream和Optional以后或许会略有改进。
而且C++有的所有问题，Java中也同样都存在。比如NullPointerException，OutOfMemoryError，IndexOutOfBoundException，甚至还有个不知所云的RuntimeException。这种设计其实就是把本来该处理的事情做了一个转移而已。
以及在try-with-resources出现之前，自动管理**资源**的机制也没有，而且出现以后也并不是那么的好用。

Java平台：
太TM多选择啦啊艹。（[Comparison of application servers](https://en.wikipedia.org/wiki/Comparison_of_application_servers#Java) 开源的就有七八种
太复杂了啊艹。（[为什么Java总被黑？ - 匿名用户的回答](http://www.zhihu.com/question/36899399/answer/69824238)
太慢了啊艹。跑个测试都可以来一盘LoL了。
太难用了啊艹。直到Java 8才把大部分C++ algotirhm里面的东西抄进来，STL已经出现快20年了啊。

Java程序员：（当然有些可能不能算
更多的人会把脑回路应用到如何处理复杂业务和异常中去，当然也有一部分像SpringSource这种的，会专心于造各种轮子来用复杂的思路去简化Java开发。
剩下的那些人更多的时间是利用**百度**和**CSDN**来写代码。

**利益相关，专业Java程序员。**
========= 原答案： =========
原来我是傻逼啊。

但谁说傻逼就不能黑Java？
