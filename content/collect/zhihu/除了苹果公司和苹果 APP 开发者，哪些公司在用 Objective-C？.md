---
title: 除了苹果公司和苹果 APP 开发者，哪些公司在用 Objective-C？
date: 2015-03-02
origin: https://www.zhihu.com/question/21142717/answer/40928617
---
# 除了苹果公司和苹果 APP 开发者，哪些公司在用 Objective-C？

[知乎链接](https://www.zhihu.com/question/21142717/answer/40928617)

---------

谢邀。

几乎没有。
早期可能会有用各种Objective-C实现来开发各种系统的，现在再用的话，估计只可能是因为历史原因不方便切换技术栈了吧。

因为使用Objective-C在非Apple的平台（iOS / Mac OS X）下开发基本**没有任何优势**。
离开了Apple的运行时和开发框架，基本上就成了一个半残废了。

新特性过度依赖运行时；比起C++，没有**标准库**；比起Java，没有那套**生态环境**；比起.NET Framework，连一个强过Mono的**开源实现**都没有。
也没有优秀的第三方开源框架用于**快速开发**，也就被Python / Ruby之类的比下去了。
利用C库做binding也不如各种简单方便的胶水语言。

另外就算有人要重新造轮子实现一套跨平台的运行时和标准库（像ObjFW），还要把周边工具（至少有一个IDE）完善了才行。这项工程不是哪个公司随便说来就来的（你看JetBrains都没敢这么玩。

谁敢用啊~！
