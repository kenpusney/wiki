---
title: c中函数指针之间的比较有什么意义？
date: 2015-05-23
origin: https://www.zhihu.com/question/29999563/answer/48756914
---
# c中函数指针之间的比较有什么意义？

[知乎链接](https://www.zhihu.com/question/29999563/answer/48756914)

---------

既然说相等和不等的比较，那就是在说[Equality Comparable](http://en.cppreference.com/w/cpp/concept/EqualityComparable)咯。
要满足reflexivity, symmetry, transitivity.
说白了还是**代数**嘛。

毕竟需要区分同一类型的不同函数，而能够区分这个的就只有函数指针了。
要从一类函数指针中区分出你想要的那个来，难道不需要进行**同一性**（Identity）比较么？而对于函数指针，只能通过判断指针的**相等性**（Equality）来确定**同一性**（Identity）了。

至于C++多态如何实现的，建议去看下：
[深度探索C++对象模型](http://book.douban.com/subject/10427315/)，
哦，另给每个看过此题目的人推荐一下：
[编程原本](http://book.douban.com/subject/7564093/)。

就是这样。
