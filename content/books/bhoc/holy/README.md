# 圣战捡屎 A Shit of Holy War

本文在我的公众号lightych连载。

编辑器篇：

- [（一）上古时代](https://mp.weixin.qq.com/s/ug80K3-zgJyCTavLkiE0-w)
- [（二）Unix 时代](https://mp.weixin.qq.com/s/1hd8_F4WQr5SQYfnYzKs9w)
- [（三）黄金时代/Emacs](https://mp.weixin.qq.com/s/_pCP7B6KvT3lO86bYWIjPQ)
- [（四）黄金时代/vi](https://mp.weixin.qq.com/s/up3yZ27rcAABMCSoFN8SUA)
- [（五）新战场](https://mp.weixin.qq.com/s/R7O5Ab0pYWI7P6htKS32mw)

## 缘起

你知道程序员是个了不得的群体，这群人其实是最宗教，最容易被煽动和感染的群体之一。每个人都多多少少的带着无数种信仰写出一行行的代码，这些信仰指导着他们的工作，学习和仅有的一部分娱乐，包括且不限于，建立鄙视链、划定群体和引发圣战。

我曾试图分析过为什么程序员们对圣战这么热衷，后面发现最终都会落地到宗教性上。任何工具或者系统，作为程序员日常的一部分，都因为习惯、崇尚的哲学和各种奇怪的原因，被作为了圣战的战场：编辑器、操作系统、程序设计语言、不同的编码习惯、不同的工程流派等等。

我个人其实很反感这种感觉，所以对任何圣战相关的话题我都会保持一个中立的态度（当然除非是为了活跃气氛吼一句，“PHP是最好的编程语言”）。毕竟，所有的工具，只有被好好使用才是有用的工具，这种很大程度上出于自身的倾向形成的圣战，只能说明个人的惰性。不过，另外值得提的一点，战争有时候是能够推进科技进步的。程序员的圣战也一样。虽然可能花在互怼上的时间一定程度上影响了效率，但相互争论之后的结果一定是某一方或者两方尝试去提升自己的实力：进而把工具、系统或者理论变得更好。

这也是为什么我想到要写简史的原因。能让我们进步的事情是值得记录和赞扬的，虽然他们本质上可能并不是为了进步。

## 从最基本的工具说起

曾经在跟同事一起pair的时候，他进到一个运行中的docker容器里面，发现找不到任何一款趁手的编辑器来编辑配置文件了。因为要知道为了尽量保证容器清量我们肯定是让容器里的东西尽可能的越少越好。这个时候就看到他有点慌，毕竟这种如果不这样做把编辑好的文件复制到内网再放到容器里这样的过程是非常折腾的。

大部分人遇到这种问题第一个反应也是，`apt install vim`。作为黄金时代编辑器的胜出者，Vim已经是dominant了。绝大多数情况下在连接远程服务器的时候最趁手的编辑工具一定就是它，这也是当年一个Vim党在向我安利Vim的时候的理由。

其实解决这个问题根本用不到安装编辑器这么麻烦，毕竟我们现在使用的是终端模拟器，比上古时代的终端好用了不知道多少倍。Linux Shell又是基于字符流的，所以用标准输入或者heredoc可以轻松实现修改文件内容的动作。只是各位基本功和认知不到位，或者没有见识过上古时代的工具，一直出于惯性地以为工具就是这个样子才行，造成的错觉罢了。

你看，了解历史多重要。

回到话题，编辑器这个东西，在上古时代就是个难题。毕竟在上古时代，“文件”这个概念可能都不存在。

### 打孔卡

这是最早的编程工具了。

如果大家有看过图灵的传记的话肯定知道最早的那个计算机是用什么来做输入的。一个个的转盘转到指定的位置，来表示输入，然后等状态输出的转盘转到特定的位置来表现表示输出。

打孔卡也一样，通过孔的状态来去区分0和1。这样有个好处就是可以通过这张卡的数量来动态的控制输入输出。但是同样还是有问题，当你的打孔卡有地方出错的时候，修改起来十分麻烦，至少某一段打孔卡你要完全重新编辑。

直到后面电子媒介产生，大家可以通过使用特定的编码来存储信息，才有了进一步使用电子输入设备编辑文本和代码的可能性。

### TECO

我们看一下上古时代的几个经典编辑器。

第一个能称道的就是TECO（Text Editor & Corrector）。它首先是一个面向字符的编辑器，其次是一个用于文本处理的编程语言。

TECO是PDP-1时代的产品。在TECO之前，有一个叫“昂贵的打字机”（Expensive Typewriter），可以接入IBM的打字机作为输入，在PDP-1上进行文字处理。这个名字的后半部分来自于另外一个早期的编辑器“巨型打字机”（Colossal Typewriter），作者是LISP之父，约翰麦卡锡；前半部分嘛，就是因为PDP-1比起打字机来贵得多了。

TECO的整体思路是为了提升PDP-1的利用率，所以在设计思路上与直接通过控制台来编辑文档的思路不同。TECO会接受两个磁带的输入，一个是源文本磁带，另外一个是更正磁带，TECO会读取更正磁带上的指令来即时修改源文本磁带上的内容。这样作为操作人员只需要实时输入指令就能实现即时编辑文档了。

所以更正磁带其实就相当于是用来做文本处理的程序，因为TECO实现的太过于复杂，以至于这些命令组合起来是图灵完全的。所以，TECO完全可以作为一个编程语言来用。

TECO的命令以及后面加入的宏足够强大，以至于后面把编辑宏（Edit MACroS）集合起来打包发布了一个应用，EMACS。

### ed 和 ex

真的等 Emacs 系出现并成熟都已经是后话了。

1969 年是个丰收的年份。AT&T 贝尔实验室的 Ken Thompson 实现了第一版的 Unix 操作系统，其中包含了三个关键的组件：汇编器、编辑器和 shell。ed 就是其中的编辑器，关键组件之一。

ed 很经典的地方在于实现了对正则表达式的支持，同时也是一个基于命令的面向行的编辑器。相较于 TECO 的复杂，ed 更多的是灵活和直接，可以直接从标准输入读入编辑命令，然后把改动反应并写入到文件中。

但相对应地也有一个很致命的缺点，就是不能实时预览编辑，只有通过特定的命令（`,l`）来查看结果。（毕竟根据 Unix 设计哲学，一个程序只做一件事情，查看文档内容应该去找 cat 或者 more。）于是也就被冠以了“对用户最不友好的编辑器”的名头。

后面自然就因为这个缺点被其他编辑器给替代了，我们虽然依然能够在系统中看到他的身影（毕竟按照 POSIX 标准，这是系统必备的程序之一），也几乎没人在用了。可在早期，这个编辑器配合 Unix shell，能够完成非常强大的自动化功能。这也逐渐催生了基于流的编辑器变种，sed。而另外一个常用的非交互式应用，也因为 ed 中的正则表达式引擎被制造出来，成为了现在搜索常用的 grep（`g/re/p`，Globally match RegExp and Print）。

另外，ed 中的大部分命令，也因为接下来的这个程序被传承了下来。

1970 年以后 Unix 在西方各个高校传播，英国 Queen Mary College 的 George Coulouris 在开发了一个 ed 的增强版，em，来更好的通过视频终端展示和做编辑。后面在 Berkeley 访问的时候，Coulouris 把他的程序展示给了 Bill Joy，后者在做了一些相应的改动之后，实现了一个扩展版，ex（EXtended）。后来这个应用就进了伯克利软件发行版（Berkeley Software Distribution），成为了知名的 BSD 系统的一部分。再之后就被连同它的“可视化版”一起加入了 POSIX 标准。

哦这个可视化版就是 vi（ex visual mode）。

后来 vi 又被分化出了一个改进版（Vi IMproved），就是基本常规桌面类 Unix 操作系统里面必备的 vim 了。

从 ed 到 vim，里面的命令几乎是一脉相承的。插入是 i，追加是 a，替换是 s，写入是 w，退出是 q。

我依稀记得有段时间还比较热衷于编辑器圣战的时候，有人非要跟我争论说 Emacs 才是最符合 Unix 哲学的，然而事实上作为一个加了扩展之后臃肿不堪的半操作系统，Emacs 既没有纯正的 Unix 血统，又实在不符合只做一件事的 Unix 哲学，所以，这方面反倒是 vi 更胜一筹。

关于 Bill Joy，后来他离开伯克利以后创立了 Sun Microsystem，跟 James Gosling 合作开发了 Java。

当然那就是另外一回事儿了。

### Edit MACroS

时间回到 60 年代末，与贝尔实验室相隔不远的 MIT，著名的 MIT AI Lab。

MIT AI Lab 是[黑客文化](https://mp.weixin.qq.com/s/8H0XKxK74dV5QqTWJ_o_1w)的诞生地，人工智能先驱 Marvin Minsky 和 John McCarthy 带领着一群人在这里发展着尖端技术。作为著名的黑客，Richard Stallman，也就是后来 GNU 项目的发起人，也在这个实验室工作。他们所使用的生产力工具就是前面提到的 TECO，一个面向字符的、运行在 PDP 系列机器上的编辑器。70 年代初，Stallman 访问了 Stanford AI Lab，并见识了他们的编辑器 E，这个编辑器比起 [TECO](https://mp.weixin.qq.com/s/ug80K3-zgJyCTavLkiE0-w) 来，有两个明显的亮点：第一，支持 WYSIWYG（What You See Is What You Get，所见即所得）；第二，作为一个所见即所得的编辑器，E 支持文件内容随机访问。跟 TECO 需要一系列的指令然后再来操作不同，你想编辑什么，直接去编辑，然后立马就能看到编辑的结果。

Stallman 立即修改了 TECO 编辑器，给加上了所见即所得的支持，顺便添加了宏功能。另外对于随机编辑的支持，E 编辑器通过使用文件格式排布来达到这一目的，而 Stallman 选择了另外的方法， 他决定增强 TECO 处理大块文件内容的能力，从而通过把文件的整体内容加载到一块来处理，来达成随机访问的效果。这一做法也影响了后期绝大部分编辑器的设计。

### Emacs

有了宏（macro）之后，新的 TECO 在 AI Lab 越来越流行，不久就累积了一大堆的自定义宏，两年后，Guy Steele 统一整理了一下这些宏，打包到一起，然后跟 Stallman 一块儿扩展了下基础工具，得到了一个新的系统，叫 EMACS。

Emacs 立即在圈子火了起来，但接下来不断 fork 和定制化的问题让 Stallman 感觉不太对劲，于是他制定了以下的规则：

> EMACS 是在公共共享的基础之上分发的，也就是说，所有的改进都必须返回给我以便于合并和分发。

这一规则也在一定程度上影响了后续 GNU 项目和自由软件运动。

说到 Guy Steele，他在我们编辑器系列的文章里可能暂时不会再出现了，但是作为 Scheme 的设计者，大部分编程语言标准（包括 RnRS-**Scheme**、TC39-**ECMAScript**、X3J11-**C**、X3J3-**Fortran**、X3J13-**Common Lisp** 以及 JLS-**Java**）制定的参与者，几乎每一次都能站在浪潮之巅为整个行业做贡献。

### 分裂

80 年代初，MIT AI Lab 分成了两拨人，后面没有继续加入 AI Lab 的人成立了 LCS（Laboratory for Computer Science），AI Lab 的人则忙于创建并商业化两个 LISP 机器（Symbolics 和 Lisp Machine Inc）。不过除了这两拨人以外还有两位教授选择保持中立，Hal Abelson 和 Gerald Sussman，这两位后来写了一本能够撩动大部分人 G 点的书，叫《计算机的构造与解释》，这本书的致谢里提到所使用的编程语言就是 Guy Steele 参与设计的 Scheme。

原本的 Emacs 只在 PDP-10 的 ITS 系统上有实现，所以一部分人延续了传统（[Not Invented Here](https://en.wikipedia.org/wiki/Not_invented_here "Not Invented Here")），选择把这个编辑器在 Lisp Machine 上重写了一遍，也就是 EINE（EINE Is Not Emacs 的[递归缩写](https://mp.weixin.qq.com/s/ffsSIGKpZp9fYqeuSlq0OA)），后来演化为 ZWEI（ZWEI Was EINE Initially）。EINE 是第一个使用 LISP 实现的 Emacs 类编辑器，后面 1978 年，Multics 系统（就是那个被 Unix 针对的操作系统）上出现了完全用 Multics Lisp 实现的 Multics Emacs，再之后的很多 Emacs，包括如今的 GNU Emacs，都是使用 LISP 系语言作为宏/扩展语言来实现。

当然也不是全部 Emacs 都会选择 LISP，1985 年的 MicroEmacs 就是个特例，它使用了一种类似 VimScript 的混合着指令及与定义函数的命令式语言作为扩展。作为一个以跨平台为目标的编辑器，MicroEmacs 早期在 DOS/Windows 上几乎是唯一的选择。几年后 Paul Fox 基于 MicroEmacs 实现了 vile（VI Like Emacs），尝试统一 vi 和 Emacs 的编辑器有优点，也可以说是试图和平解决圣战的先驱了。另外，Linus Torvalds 在 kernel.org 托管了一份基于 MicroEmacs 3.9 版本 fork 的编辑器作为自用。

其他的实现还包括 1981 年 James Gosling 写的 Gosling Emacs，是第一个 Unix 系统上的 Emacs 类编辑器，使用 C 语言编写，用 Mocklisp 作为扩展。

基调上已经把 Emacs 和 Lisp 绑定了，为什么突然这一节就叫分裂了呢。AI Lab 分裂出去了 LCS，同时自身又分成了 Symbolics 和 Lisp Machine Inc，这导致 AI Lab 整体分裂成了好几个派别，许多人才因此流失。Richard Stallman 因此启发，创立了 GNU 项目，通过自由软件来聚集人类知识而不是划立派别组织知识的传播。

另外提一句，GNU 完整形式是 GNU's **\*\*NOT\*\*** [**Unix**](https://mp.weixin.qq.com/s/1hd8_F4WQr5SQYfnYzKs9w)。

还有，James Gosling 就是 Java 之父，在泛型尚未加入 Java 之前对 Java 有主要贡献的三个人已经全都出现了。

### VI

[如前所述](https://mp.weixin.qq.com/s/ug80K3-zgJyCTavLkiE0-w)，（原始的）vi 并不是一个单独的软件，而是 ex 的可视模式的硬连接。Bill Joy 意识到，大部分人用 ex 更多的时候会用可视模式，所以干脆直接把可视模式作为一个单独的命令来更快捷地让人访问到。

Joy 在 1979 年六月左右就不再参与 vi 的开发了。一部分原因是他觉得跟 Emacs 的非模式化的界面和强大的编程能力，对于 vi 来说是一个很强的冲击，因为本质上 vi 依然还是 ed 的模式，通过各种命令来控制。“我真希望我们没有用光键盘上所有的键。”他说。

1979 年之后，Mark Horton 接管了 vi 的开发，添加了对功能键和方向键的支持，添加了宏功能。

### 新势力

vi 在 Bill Joy 离开伯克利之后不久就交给 AT&T 接管了。但是因为 Bill Joy 最初的代码源自于 Ken Thompson 的 ed，所以在没有 AT&T 代码许可下是不能传播的。这个时候大家能够选择的 Unix 平台免费编辑器也就是 MicroEmacs。1987 年 6 月，Tim Thompson 才开发了一个功能有限的免费 vi 类编辑器 STEVIE（ST Editor for VI Enthusiasts），之后的 1990 年初，Steve Kirkendall 在 comp.os.minix 新闻组发布了 Elvis，相对 STEVIE 功能增强了很多，也更靠近 vi 的编辑习惯。

不久之后，芬兰赫尔辛基大学的 Andrew S. Tanenbaum（又叫 ast）二选一选择了 Elvis，作为他课堂用操作系统 Minix 中的编辑器。对了，ast 有一个知名的学生，上了他的操作系统原理课以后，自己动手写了一个丢到了新闻组里，这个系统就是 Linux，这个学生就是前文提到[还在用 MicroEmacs 的 Linus Torvalds](https://mp.weixin.qq.com/s/_pCP7B6KvT3lO86bYWIjPQ)。

你看这个圈子绕来绕去还都是自己人。

1989 年 Lynne Jolitz 和 William Jolitz 开始把 BSD 移植到 386 架构上，但是如果要把这个移植的系统作为自由软件发布，就需要避免任何 AT&T 相关的代码，包括原本 Bill Joy 的 vi。他们选用了 Elvis 作为 1992 年发布的 386BSD 系统 vi 的替代品，后续的 FreeBSD 和 NetBSD 也直接沿用了 386BSD 的决定。之后 Keith Bostic 在维护 BSD 4.4-Lite 的时候，希望替换掉 vi，于是在 Elvis 1.8 的基础之上开发了 nvi。FreeBSD 和 NetBSD 后续同步了 BSD 4.4-Lite2 的代码，也同时把 nvi 放到了自己的 codebase 里，作为默认编辑器使用到现在。

另外一边，随着 STEVIE 编辑器持续更新，Bram Moolenaar 基于 STIEVE 的代码在 Amiga 系统上创建了 Vi IMitation，就是后来的 Vim。Vim 在 1991 年正式公开发布，后续才逐渐成为另外一个主线。


### 集成开发环境

花开两朵，各表一枝。

1970年后个人电脑出现并流行，带动着大家逐渐注目这个方向。这个时候还没有一个成型的Unix能够放在PC上。虽然AT&T也出了一个PC用的Unix系统，但一来需要专门硬件，二来AT&T的授权费也不是一般人能给得起的。所以各种PC上的操作系统慢慢开始流行起来，包括DOS、CP/M 和 OS/2。

当然也包括PC端专门的应用软件。Basic是早期被广泛接受的编程语言，在Altair PC、Apple甚至是Atari和Nintendo的家用机上都有BASIC的实现。使用起来也很简单，你在一个编辑器里敲好BASIC代码，保存，然后执行就是了。

直到一个叫Borland的公司推出了一款产品改变了这一切。

### Turbo Pascal

1981年，来自丹麦的Anders Hejlsberg（没错，就是那个男人！）为NasSys操作系统实现了Blue Label Pascal编译器。Borland买下了这个编译器的核心部分（PolyPascal），添加了部分UI和编辑器功能，作为Turbo Pascal发布。Anders也随后加入Borland，成为了Turbo Pascal全系列和后期Delphi的架构师。

在Turbo Pascal出现之前，通常写代码都会经过两到个步骤：使用编辑器编辑文件（Edit）、调用编译器编译文件（Compile）以及链接成可执行文件（Link）。Anders的编译器实现了一遍（one-pass）编译的流程，直接省去了额外的链接操作，在Turbo Pascal里面，你可以直接点一个按钮，就进行编译运行了，如果任何地方有错都会直接给你提示在界面上。

在当时这是非常超前的技术，微软的Charles Petzold老爷子当年对此都赞不绝口。这一方便的特点也使得Turbo Pascal成了当时最受欢迎的编程语言类软件，两年内即售出去了25万多份。

另外，由于性能极度出色（第一版Turbo Pascal是完全用汇编实现的），也成了其一个标志性的卖点，同时也是Turbo这个名字的由来。甚至在Delphi时期，“编译速度快”这一点都依然能够作为一个突出的特性去正面怼隔壁的C++程序员，当然这就是后话了。

### Visual / 可视化编程

1973年，Xerox PARC实验室的Alan Kay 给 Smalltalk 设计了图形界面。不久之后这套设计就先后被Apple、Commodore和Symbolics等几家大佬看上了，先后推出了几款产品都加入了图形用户界面（GUI），WIMP的概念逐渐被接受扩展成为主流。这些相继都对后来流行的Windows操作系统产生了重要的影响。

说到Windows了，就来说一说微软对Turbo Pascal的反击，Visual Basic。

Visual系列就是顶着图形化时代的可视化编程环境的名头出现的，相比起来一个可以编码并且自动编译运行的集成开发环境，Visual Basic引入了窗体设计系统，并引入了“控件”（control）的概念，任何你想要实现的UI，只要通过控件拖拽就可以了。而且，在能力满足的情况下，你也可以通过编辑代码来实现更多高级的功能。在这之前能够实现可视化编辑功能的还有NeXTSTEP的Interface Builder，但那是作为一个额外的应用存在，并没有作为IDE的部分，后来经Apple的手才集成到Xcode中。

Visual Basic的成功非常持久，尤其是1998年的Visual Basic 6.0，在18年后的2016年，还获得了第19届D.I.C.E.奖。而且因为微软“后相兼容”原罪，至今仍然有一部分人坚持在用。竞争对手Borland早已在2009年倒闭了。

### Delphi

然后轮到了Borland的回合。作为反击的第一步，也直接推出了可视化的IDE，Delphi。同时开发了作为可视化和RAD平台的核心，Visual Component Library（VCL）。

VCL作为一个创新性的框架，除了本身支持图形化界面框架之外，还引入了事件机制把常规的继承扩展实现GUI的方式的方式变成了组合委托。并且VCL作为Borland公司的基础库，直接做到了跨语言，在C++ Builder里也可以直接编写/调用Delphi的组件。

.NET框架受VCL影响很大。并且，在1995年，微软从Borland挖过来了包含Anders Hejlsberg在内的数十个员工，来搞后面的J++和.NET。

至于Borland，2009年被Micro Focus收购之后品牌就shutdown了。所有的IDE打包成Codegear出售给了Embarcadero。所以现在作为RAD平台的Delphi还在，只是因为语言太小众（Object Pascal），没几个人用而已。

## xxx是最好的编程语言

### 还是得提一下打孔卡

### 汇编语言

### 编程语言世代

### 毒瘤

### Goto 被认为是有害的（EWD）

### FP
