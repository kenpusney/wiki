---
title: 通过读一种脚本语言（如 Python）的源码来自学编译原理是否可行？
date: 2019-04-11
origin: https://www.zhihu.com/question/318566238/answer/647723779
---
# 通过读一种脚本语言（如 Python）的源码来自学编译原理是否可行？

[知乎链接](https://www.zhihu.com/question/318566238/answer/647723779)

---------

不靠谱。

先不说cpython的Parser那堆各种生成代码的黑魔法，单是一个简单的手写parser（比如lua），也只能给你一种“哦原来看起来这么简单”的感觉，真的写起来还是到处都是坑。

所以最好的办法还是自己选择/设计/抄袭一套语法然后实现一个完整的从解析到生成/执行的编译系统，无论是通用编程语言、DSL还是什么其他的东西都行。这个时候再回头看什么理论书都比较简单了就。

Learn by doing才是制胜之道。

另同样推荐楼上的那本Understanding Computation（《计算的本质》，但是建议看英文原版），一本step by step把那些理论性的东西具象出来的书。只是没有涉及太多跟parsing相关的内容，另结合一些别的书籍会更好。<del>（比如 [@vczh](https://www.zhihu.com/people/0970f947b898ecc0ec035f9126dd4e08) 通常推荐的 Parsing Techniques（雾</del>

以上。
