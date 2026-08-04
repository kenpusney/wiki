---
title: 本人是swift小白一个，想问一下为什么xcode中不能加入根号，如何解决这样的问题？谢谢
date: 2015-04-29
origin: https://www.zhihu.com/question/29863627/answer/46266922
---
# 本人是swift小白一个，想问一下为什么xcode中不能加入根号，如何解决这样的问题？谢谢

[知乎链接](https://www.zhihu.com/question/29863627/answer/46266922)

---------

谢邀。
```text
prefix operator √ {}
prefix func √ (number: Double) -> Double {
    return sqrt(number)
}


```


参考：
[Swift Operators](http://nshipster.com/swift-operators/)
