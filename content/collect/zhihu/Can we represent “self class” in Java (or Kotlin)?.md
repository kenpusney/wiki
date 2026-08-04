---
title: Can we represent “self class” in Java (or Kotlin)?
date: 2017-12-18
origin: https://www.zhihu.com/question/264242634/answer/278438392
---
# Can we represent “self class” in Java (or Kotlin)?

[知乎链接](https://www.zhihu.com/question/264242634/answer/278438392)

---------

手机打的，可能是个解决方案。（回头电脑上换下格式）

===========

如其他答案所说，通常使用泛型可以实现你想达到的效果：

[Curiously recurring template pattern](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern)

```java
interface Fuck<T extends Fuck<T>> {
    T shit();
}
class Shit implements Fuck<Shit> {
   ...
}
```

关于评论中提到，这个用法是is-a关系的antipattern这种情况，我觉得是不对的。

这种场景下继承已经不再只是**面向对象**中的继承，更多的是用于表示类型Shit是具有Fuck中描述的行为的这样一种约束。更有点像是Concept或者typeclass。

比如我想实现一个能够接受所有实现了Fuck的类型的方法，那么只需要：

```java
<T> fuck(Fuck<T> f) {
    f.shit() // <- compile time type: T
}
```

这个时候我的编译时类型依然是T，这应该才是题主预期的行为。

另外，既然超类型是Fuck<Shit>（而不是Fuck，注意区别），我有一个 Shit shit()的方法在也并没有造成任何问题，在任何出现Fuck<Shit>的地方都依然可以用Shit来替换。是符合Liskov替换法则的。毕竟，泛型类型，而且又是返回值，又是满足了Shit<Fuck>的约束，为什么不能作为超类对象用呢。

另外一个问题就是，这个不是fool-proof的，也就是说不能避免有人非要写：

```java
class Dick implements Fuck<Shit> {
   ....
}
```

这个嘛，我也没办法。毕竟想要不按规矩来办事的人，远比能遵守规矩的人多。

其三就是为什么会有这个需求。

对于[@正逍遥0716](https://www.zhihu.com/people/95e2ac2140323117a47e3eb41fa35ed3) 给出的解决方案，我们可以看题主在题目中是怎么说的：

> Say, I want to **force **every A's subclass' bla method to return their self, instead of an A.

注意force，也就是说如果你不这么搞就要compile error（或者题主说的type error）才对。

所以我猜题主的意思是要充分使用编译器的type checker来辅助静态类型推导，而不是type eraser或者reflection来去猜具体的类型。

以上。
