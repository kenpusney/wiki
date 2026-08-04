---
title: 如何评价 Herb Sutter 的 C++ 提案：metaclasses？
date: 2017-06-28
origin: https://www.zhihu.com/question/61675549/answer/190459661
---
# 如何评价 Herb Sutter 的 C++ 提案：metaclasses？

[知乎链接](https://www.zhihu.com/question/61675549/answer/190459661)

---------

啥时候加入template metaclass让metaclass支持参数化啊。

```text
template<class T>
$class mixin 
{
   ...
};

mixin<Fuck> Shit 
{
   ...
};
```

==========

又细看了一遍，原来已经打算包含进去了。

其实相当于搞了一套针对class的宏，能够更自然地利用static reflection的信息来开心地艹代码。

HS终于在追赶AA的路上又迈进了一大步啊。希望他们能够胜利会师。
