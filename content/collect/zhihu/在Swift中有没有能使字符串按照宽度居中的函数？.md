---
title: 在Swift中有没有能使字符串按照宽度居中的函数？
date: 2015-03-15
origin: https://www.zhihu.com/question/28784304/answer/42087885
---
# 在Swift中有没有能使字符串按照宽度居中的函数？

[知乎链接](https://www.zhihu.com/question/28784304/answer/42087885)

---------

至少目前来说，我不知道。
但是你可以自己搞一个。
```text
extension String {
    func center(width:Int) -> String {
       // ... and so on
    }
}
```


//点赞可以得到更多的提示哦！
