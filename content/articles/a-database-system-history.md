---
title: 数据库系统简史
public: false
---

# 数据库模型简史

1974年的加利福尼亚圣何塞，埃德加·科德（Edgar F. Codd）和克里斯托弗·达特（Christopher J. Date）在SIGMOD组织的一场Workshop上发表了一篇名为Interactive Support for Nonprogrammers: The Relational and Network Approaches的论文。在这场后来被人称为“大辩论”（The Great Debate）的Workshop上，Codd 展示了他多年来一直在开发的关系数据模型和来自于CODASYL的网络数据模型之间相互的优缺点。数年之后，随着INGRES和System R相继验证了关系数据模型以及Oracle和DB2商用数据库的出现，关系数据库模型逐渐成为了绝大多数数据库系统的核心模型。

## 前关系模型时代

我们以关系型数据库系统出现为分界线，往前看一下数据库还有哪些形态。

最早也最直接的实现是flat file。也即单纯往一个文件里直接写入数据记录。这个时候是不存在，或者说没有普遍意义的“数据库系统”的。每一个应用程序都可以定义自己所采用的格式来存储和访问具体的数据。优势当然是简单直接，缺点也自然是因为其简单而丧失了扩展性，任何额外需要的功能都要用过修改应用程序来实现，而且在表现复杂数据关系这方面几乎没什么能力。这种形式的数据库因为其简单至今还存在，比如Unix系统中的 `/etc/passwd` 文件，就是操作系统的“用户数据库”。

