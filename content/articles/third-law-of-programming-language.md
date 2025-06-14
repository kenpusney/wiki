---
title: 第三定律
draft: true
date: 2023-04-11
----

事情源于对传统Java NIO的<del>褒奖</del>。众所周知，因为NIO的出现，给JVM带来了ByteBuffer这么一个神器。于是各种你想象不到的传统操作，都可以想象甚至能够实现了。这种通过硬拗ByteBuffer来强行扩展应用范围的操作，属实是拓展了生态圈。按照Tison老师的说法，这证明了Java有实现存储系统的能力。我觉得我们可以放远一些看，这其实说明了，Java是能胜任系统编程（System Programming）的。

这跟所谓第三定律有什么关系呢？首先，既然是第三定律，那么前面肯定还有两个定律。如同列位即将看到的第三个一样，前两个也是我纯属主观角度的总结。主要是为了定性去分析编程语言，以及他们的适用范围。

我们来依次看看这三条定律。

### 第一定律

第一定律的直接表述是：

> 一切编程语言都是 DSL（领域特定语言）。

这条定律还有个早期表述，后面甚至因此跟知乎的一个老哥打过赌。但是这个早期表述一定程度上是跟今天的第三定律有冲突的，所以暂时就不提了。改天方便可以单开一篇特别讲讲相关内容。

总之，第一定律主要想表达的就是，别种想着拿着锤子看什么都是钉子。有些东西他就只适合在特定场景下用。毕竟 Fredrick Brooks 老爷子也说过嘛，**没有银弹**。

理想情况下我们当然希望有这么一个通用编程语言存在。但，早在之前我就[提过相关观点](https://mp.weixin.qq.com/s/Gqo0if2UNNcp1Q9XHlm4mA)，历史和现实决定了这件事情是不可能的。

当然放在现在也许会有人说，自然语言就是最好的编程语言了，你不是可以跟 AI 对话来达成各种目标嘛。这话听起来挺有道理的，但是大语言模型改变的只是终端用户的人机接口。AI可以代替你去写代码了，但是写出来的代码，不依然是Python、Java或者Swift之流吗？

### 第二定律

第二定律相对比较简单，就是如何判断一个编程语言或者编程平台的可用性。

> 只有当一个编程语言/平台有了对应的测试框架，这个平台才能做到Production Ready。

大概两年多以前的《[Low-Code 三问](https://mp.weixin.qq.com/s/owaHwkdCladyqkL3pL7o6A)》中，这就是我提出的其中一个的问题。如果一个语言和平台可以提供可用的工具来进行逻辑上的验证，那相对来说在上面进行构建和变更的时候，可靠度就是可以保障的。做不到这一点的话，只能是个玩具。

这个定律同样地可以应用到目前流行的生成式 AI 应用。参考[前文](https://mp.weixin.qq.com/s/pH7SX3QgB_VtwnphPTO4fQ)中我提过的 ChatGPT 的缺点，因为他没办法提供引用来源，所以可信度是大打折扣的，任何生成的内容都必须靠我人肉来判断他的可信度，于是他只能作为一个辅助性的工具来用。

### 第三定律

第三定律的目前的表述方式是限制了范围的，但其实可以推广到更多特性上：

> 任何声称能进行系统编程的编程语言，必然以某种方式重新发明了ByteBuffer。

也就是说，这条定律是个pattern，即“任何声称xxx的编程语言，必然以某种方式重新发明了yyy”。比如你把 xxx 替换成“能进行编译期计算”，把 yyy 替换成“预处理宏”，效果不变。模板、宏、语法扩展、编译器插件、生成器，本质上都是一样的，换了个盘子端上来喂给你而已。

说回 ByteBuffer，为什么这个点这么重要。毕竟大多数编程语言如果拥有 C binding 大概也能做到一样的效果。但是 C binding 毕竟只能是个 C binding，与本身属于该语言的一部分还是有着隔阂的，任何数据都要通过原本的 C 库和该语言的代码之间相互翻译。这一点，微软在构建 VS Code 时也提过，因为 JS 跟 C++ 的通信之间需要大量的数据格式转换，结果后面直接替换成了 JS 实现反倒效率更高。

> We built a text buffer implementation in C++ and used native node module bindings to integrate it in VS Code. The text buffer is a popular component in VS Code and thus many calls were being made to the text buffer. When both the caller and the implementation were written in JavaScript, V8 was able to inline many of these calls. With a native text buffer, there are JavaScript <=> C++ round trips and given the number to round-trips, they slowed everything down.
>
> <small>_[Text Buffer Reimplementation](https://code.visualstudio.com/blogs/2018/03/23/text-buffer-reimplementation)_, **Visual Studio Code Blog**</small>

能否给你一个硬拗 ByteBuffer 的能力，决定了在实现一些关键组建的时候所表现出来的可用性和性能的优势有多少。如果说第一定律是给每个编程语语言一个纵向的定位，那不同编程语言其所能应用到第三定律模式上的特性越多，越能说明其横向的覆盖范围。

然后你会看到，那些覆盖得广的编程语言，都是些难以被常人所掌控的怪物。这也反过来说明了第一定律的普适性。

以上就是这三条定律的全部内容。没什么特别复杂的，就是偏主观一些的定性分析。也许后面还会增删或者变更表述，到时候就再更新吧。