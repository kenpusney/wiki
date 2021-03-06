---
title: 又一个上古神器开源了，GW-BASIC
date: 2020-05-22
---

最近微软发布了一则新闻。他们[把 30 多年前的 Microsoft Basic 开源了](https://devblogs.microsoft.com/commandline/microsoft-open-sources-gw-basic/ "Microsoft Basic 开源了")。很高兴微软能够这样积极的[拥抱开源社区](https://pulse.microsoft.com/nl-nl/business-leadership-nl-nl/na/fa1-microsoft-loves-open-source/ "Microsoft Loves Open Source")，也特别期待能够进一步看到微软开放出来更多的系统。

**BASIC** 对于微软来说是一个非常重要的语言。微软的第一桶金就是**比尔·盖茨**和**保罗·艾伦**在 70 年代的 **Altair 8800** 上面开发的 Altair Basic。随后 Basic 作为一个基础的软件，进入到了不同的软件平台，特别在 70 年代末 80 年代初个人计算机刚刚兴起的年代 **Commodore 64**、**Atari 2600** 甚至是 **NES**（红白机）上面都有 basic 的实现。

![日版（FamiCom）的Family Basic，附件是一个键盘——是不是像极了小霸王（雾）](https://imgkr.cn-bj.ufileos.com/1dd9348e-cf1b-4cf3-a188-1c21dd3af972.jpg)

可以说那个时代的 Basic 相对来说比当今的 Python 还要流行，比生化危机 4 和上古卷轴 5 所跨的平台还要多。在早期 C 语言还没有成为各个操作系统标配接口的时候，Basic 可是给基础用户使用的一个标准接口。而微软就成了 Basic 界的扛把子。在很长的一段时间内，各种家用电脑上的 Basic 软件都由微软来供应，并且在十多年后，微软发布了知名的 [Visual Basic](https://mp.weixin.qq.com/s/2F2g9WeIAqVwn03jpg3oiA)，而其中的 Visual Basic 6.0，直到又过了 20 多年后的今天，还有人在用。

![SmileBASIC for Nintendo Switch](https://imgkr.cn-bj.ufileos.com/227f58a5-ec23-48e7-ac29-2e98b45145fa.jpg)

这次开源的 GW-BASIC 完全是汇编代码。因为在 70 年代 80 年代的时候，[Unix 和 C 语言](https://mp.weixin.qq.com/s/1hd8_F4WQr5SQYfnYzKs9w)还仍然是属于实验室和院校研究使用的工具。个人电脑上可享受不到这么高大上的东西。但好在当时的平台都有着比较相似的架构和指令集，无非在细微上有所区别，因此要想通过汇编来实现一些应用是相对比较容易的，因为那个时候已经出现了结构化变成了思想。毕竟早在 1968 年，Dijkstra 先生就已经发表了著名的[Go To Statement Considered Harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf "Go To Statement Considered Harmful")论文。

![比尔·盖茨、Popular Electronics 和 Altair 8800](https://imgkr.cn-bj.ufileos.com/877f393a-29e6-4bdc-9d07-1bb317f5aed5.jpg)

前面说的最早的 Basic 是**比尔·盖茨**和**保罗·艾伦**一起实现的。但在现在这个开源的版本里面应该没有他们两个人的代码了。按照微软官方的说法，GW-BASIC 的代码是从某种源代码翻译到 **Intel 8088** 汇编的。因为早期的计算机架构都比较接近，而大部分的软件又都通过汇编语言来实现，所以，微软就使用了转译的方式来把 Basic 移植各个平台。这样就省去了分别维护不同平台代码带来的工作量，也是早期的元编程操作吧。

![单单是6502一个平台就有很多Basic变种](https://imgkr.cn-bj.ufileos.com/ceab9b81-97b0-402e-8d5a-d0bfb2ee64bc.jpg)

即便这是生成的代码，即便这已经是这已经是几十年间的内容了，这个经久不衰的编程语言以及跟它相配套的 MS-DOS 操作系统——微软在去年也已经开源——都是比较值得研究的对象。最近这两天我还一直在看 6502 架构的 [Commodore 64](https://www.bilibili.com/video/BV1ex41167ZK "关于 Commodore 64 的一切") 和 [Atari 2600](https://www.bilibili.com/video/BV1ix411J7xt "关于 Atari 2600 的一切") 的实现细节。这个时候你去了解和思考思考他们所面临的问题和解决方法，对从宏观角度认识和分解一个系统帮助非常的大。

![一代传奇 Commodore 64](https://imgkr.cn-bj.ufileos.com/e51a93a3-c805-43f2-b2a7-c9e3739a0e9c.jpg)

好的，关于这些上古神器，我们今天就说这些，祝大家周末愉快。
