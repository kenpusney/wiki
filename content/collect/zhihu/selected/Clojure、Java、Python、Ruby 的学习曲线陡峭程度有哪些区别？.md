---
title: Clojure、Java、Python、Ruby 的学习曲线陡峭程度有哪些区别？
date: 2014-10-11
origin: https://www.zhihu.com/question/25688042/answer/31698661
---
# Clojure、Java、Python、Ruby 的学习曲线陡峭程度有哪些区别？

[知乎链接](https://www.zhihu.com/question/25688042/answer/31698661)

---------

分别是：
$$O(2^{n}), O(n), O(n^{2}), O(n \cdot \log  n) $$

横坐标表示progress，纵坐标表示cost。

- 关于 **Clojure**，完全同意另外一位不愿意透露姓名的答主的[[#引用的匿名答主的回答|答案]]。
- 关于 **Java**，没有过于复杂的概念，只有过于繁杂的操作。只要你耐心慢慢来，进步就一定会有。而且还有SpringSource这样的业界良心在想尽方法帮助你升级。
- 关于 **Python**，前期看起来语法简单清晰，易于学习。过了入门这个坎之后，就是一个个苦逼的坑在等着你。
- 关于 **Ruby**，首先得习惯他的风格（do...end / gem / \*-driven / 各种DSL），做到这件事儿之后，接下来的就不是问题了。

另外， [@huayi](https://www.zhihu.com/people/32a840d2eff15a0880041ddd4f47832d)推荐的教程拿来入门很是赞。不过如果综合去考虑一门语言的学习曲线，我觉得需要把后面会用到的高级内容也算在内吧。

以上。


### 引用的匿名答主的回答

来自知乎[^1]。

> Clojure 的难点有三个：
> 1. 对于 Java 程序员来说，Clojure 是一种 lisp、基于 immutable types，语法和思维方式完全不同
> 2. 对于 Lisp 程序员来说学 Clojure 要掌握大量的 Java 类库、JVM 相关知识
> 3. 对于其它程序员来说，Clojure 有大量的符号，大量的平铺的函数（[Overview - Clojure v1.6 API documentation](https://clojure.github.io/clojure/)），缺乏一个逐步了解的「线索」


[^1]: https://www.zhihu.com/question/25688042/answer/31489316
