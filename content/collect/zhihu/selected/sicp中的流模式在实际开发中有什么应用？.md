---
title: sicp中的流模式在实际开发中有什么应用？
date: 2015-06-19
origin: https://www.zhihu.com/question/31423936/answer/51875751
---
# sicp中的流模式在实际开发中有什么应用？

[知乎链接](https://www.zhihu.com/question/31423936/answer/51875751)

---------

谢邀！

你的感觉没错，iterator模式就是一个典型的例子。
如果还觉得不对劲的话，可以看看C++ Range Proposal（[D4128: Ranges for the Standard Library: Revision 1](https://ericniebler.github.io/std/wg21/D4128.html)）。

延时计算使用非常广泛，比如[Futures/promises](https://en.wikipedia.org/wiki/Futures_and_promises)（当然其中已经不仅仅是延时了），比如Python的yield，比如C#的async/await。

还有像Haskell这样的编程语言，本身就是lazy by default的。

一方面，就是call by need，也就是说，在我需要的时候才会求值，不会浪费太多的计算在无用的事情上。

> 比如你要去读一个文本文件特定的某一行，等待以后处理，lazy的话，只是会保存你的文件句柄和行号，在你真的要对该行文本处理的时候才会去读取然后处理，而非lazy的处理过程可能会是直接打开文件，读取到该行文本，然后直接交给你。（嗯，就是I/O Stream）

另一方面，这种设计可以增强任务的异步性和并行性，也就是说，我可以把要计算的东西切换到另一个线程/进程去执行，等他得到结果之后我可能才会需要对其处理。一个很明显的例子就是Promise模式。

延伸一点的话，像[libevent](http://libevent.org/)这种都算是类似的应用。

另外，C++怎么就没有延时求值了？Functor / Iterator / Stream / Lambda又不是摆设。

以及：[lazy.c](https://gist.github.com/kenpusney/4db995e8b774826ff1c7)（一时找不到例子了自己弄了个丑的）
