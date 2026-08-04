---
title: 能用VHDL语言写一个操作系统吗，实时操作系统之类的？
date: 2015-01-17
origin: https://www.zhihu.com/question/27367977/answer/37449084
---
# 能用VHDL语言写一个操作系统吗，实时操作系统之类的？

[知乎链接](https://www.zhihu.com/question/27367977/answer/37449084)

---------

我的结论是**能**。

嘛，这么设想一下吧。
> 假如有那么一个HDL能够实现一个OS，那么跑在这个OS上的各种各样的**task**是什么呢？


OK换一个问题，
> 假设我的一个用HDL写的OS已经做成了IC了，那么怎么对这个IC进行**扩展**呢？

没错我连上另外一个（也许是多个）IC不就结了。

所以拿HDL写一个实时的操作系统，权当是实现一个有限的Scheduler + Channel，再定义一套Protocol，然后接着拿HDL去写task跑吧。

那么问题来了。
1、成本。
2、开发效率。
3、测试（行话叫**验证**）。
如果这几个问题得不到解决，实现出来也不现实。
拿来玩玩还是可以的。

参考：[http://book.douban.com/subject/3359818/](http://book.douban.com/subject/3359818/)
