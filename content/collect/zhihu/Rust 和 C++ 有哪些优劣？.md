---
title: Rust 和 C++ 有哪些优劣？
date: 2015-02-07
origin: https://www.zhihu.com/question/27608498/answer/39150664
---
# Rust 和 C++ 有哪些优劣？

[知乎链接](https://www.zhihu.com/question/27608498/answer/39150664)

---------

记得[http://Rust.cc](http://Rust.cc)社区的Mike Tang提到的很重要的一点。
“**Rust为了安全几乎可以放弃一切。**”
当然这里的**安全**指的是safety，而不是security。
为了保证这一点Rust引入了很多东西，比如前面很多人都提到过的borrow checker和lifetime以及强约束的generic等等。

当然，踩过C++坑的都能够理解为什么会这么设计，C++也是在冲着这个方向发展。
但是反过来你要跟一群熟悉了使用引用（指针）和GC的人说明白什么是borrow，什么是move，什么是lifetime，以及为什么要如此设计对象模型等，还是很困难的。
毕竟不像Go或者Swift，估计培训机构一时半会儿也理解不了这些东西。（想想同样是14年的新生语言的**Hack**吧。

所以，如果真的出现了支持Concept、Module和Reflection的C++1z、2z或者3z，我就不那么热爱Rust了。
