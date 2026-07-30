---
title: Meta wiki
date: 2017-01-17
---
这里包含本Wiki相关的文档和一些工具、使用方法以及观点的介绍，以及历史。

目前你看到的内容是由 Obsidian 驱动，由 Material for MkDocs 渲染的站点。我在2016年考虑使用的关联思路已经太老旧了，现在基于 Zettelkasten 的笔记构建工具非常方便，加上我本来也就是按照主题分类，也是用于构建我的出版系统，所以很自然的就结合起来了。在这之前我也曾经换成过Logseq，但是各方面的问题[^1] 导致了我最终不得不重新考虑笔记系统，然后发现其实整体也可以把Wiki这里给替换了。

## 历史

这个站点最初只是一系列的静态HTML页面，来托管我想要分享的内容，包括一个Lisp Interpreter，以及一个用来展示 Wikipedia 相关页面关系的一个 Graph（非常接近现在 Obsidian 的 GraphView）。早期的域名是 `lisp.kimleo.net`，站点名称叫做 im Leo's PLT Collection。2016年加入更多内容以后改成现在的域名。

2016年5月份开始第一版的动态页面设计。最早的就是 [[测试页面]]。并且最早的文档并非后来的 CNMD，而是单纯的 txt 文件（虽然格式还是Markdown）。这个时候的页面只有一个 `index.html`，获取路由内容加载对应的 Markdown 文件。一周以后对应的格式被我改成 `*.cn.md`，这样能充分利用编辑器的 Markdown 高亮的同时还能跟普通的 Markdown 文件作区分。

2016年11月，这个站点正式改名为 **Kimmy's Wiki**。

2017年折腾了很多，比如企图加入一个 command line tool 来辅助创建和管理页面，加入了索引和搜索的代码。甚至尝试加入一组专用的 command 来设计创建和 fork 整个  Wiki  体系。相当多的内容都被归档了[^2]，包括一组专用的生成工具[^3]。你可以从 [[Workflow of this wiki]] 里看到当时的设计。

2019年4月，原本简单的 HTML/AMD 代码使用 React 重写。随后加入更加复杂的体系来还原当时的索引逻辑，并且尝试实现 TFIDF 的方式来提取关键字。

2020年7月17日，尝试替换成 Hugo 无效后，开始着手手动实现生成器。2020年8月23日，切换到正式的手动生成器。手动生成器的内容参考 [[新版Wiki的设计]]。

2025年11月，替换成 Logseq 格式，通过 Logseq 自动导出站点内容。

2026年7月，替换成 Obsidian 格式，通过 Material for MkDocs 生成站点。


[^1]: Logseq各方面的问题我会总结一篇文章来分享。

[^2]: wikiflow-ruby https://github.com/kenpusney/wikiflow-ruby

[^3]: poi https://github.com/poi-templates/poi
