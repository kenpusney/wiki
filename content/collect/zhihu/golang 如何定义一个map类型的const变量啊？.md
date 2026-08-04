---
title: golang 如何定义一个map类型的const变量啊？
date: 2014-10-11
origin: https://www.zhihu.com/question/25953192/answer/31698236
---
# golang 如何定义一个map类型的const变量啊？

[知乎链接](https://www.zhihu.com/question/25953192/answer/31698236)

---------

。。。虽说Go加入了[Composite literals](http://golang.org/ref/spec#Composite_literals)，也不是这种蛋疼的用法吧。
其次，Go哪有所谓的const map这一说？
去看下spec吧：
[http://golang.org/ref/spec#Constants](http://golang.org/ref/spec#Constants)
[http://golang.org/ref/spec#Constant_expressions](http://golang.org/ref/spec#Constant_expressions)
另附上题主所期望的效果的正确写法：
```go
romanNumeralDict := map[int]string{
  1000: "M",
  900 : "CM",
  500 : "D",
  400 : "CD",
  100 : "C",
  90  : "XC",
  50  : "L",
  40  : "XL",
  10  : "X",
  9   : "IX",
  5   : "V",
  4   : "IV",
  1   : "I",
}

```
