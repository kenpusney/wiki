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

关于评论中提到，这个用法是 is-a 关系的 antipattern 这种情况，我觉得是不对的。

这种场景下继承已经不再只是**面向对象**中的继承，更多的是用于表示类型 `Shit` 是具有 `Fuck` 中描述的行为的这样一种约束。更有点像是 `Concept` 或者 `typeclass`。

比如我想实现一个能够接受所有实现了 `Fuck` 的类型的方法，那么只需要：

```java
<T> fuck(Fuck<T> f) {
    f.shit() // <- compile time type: T
}
```

这个时候我的编译时类型依然是T，这应该才是题主预期的行为。

另外，既然超类型是`Fuck<Shit>`（而不是Fuck，注意区别），我有一个 `Shit shit()` 的方法在也并没有造成任何问题，在任何出现 `Fuck<Shit>` 的地方都依然可以用 `Shit` 来替换。是符合Liskov替换法则的。毕竟，泛型类型，而且又是返回值，又是满足了 `Shit<Fuck>` 的约束，为什么不能作为超类对象用呢。

另外一个问题就是，这个不是fool-proof的，也就是说不能避免有人非要写：

```java
class Dick implements Fuck<Shit> {
   ....
}
```

这个嘛，我也没办法。毕竟想要不按规矩来办事的人，远比能遵守规矩的人多。

其三就是为什么会有这个需求。

对于[@正逍遥0716](https://www.zhihu.com/people/95e2ac2140323117a47e3eb41fa35ed3) 给出的解决方案，我们可以看题主在题目中是怎么说的：

> Say, I want to **force** every A's subclass' bla method to return their self, instead of an A.

注意 force，也就是说如果你不这么搞就要 compile error（或者题主说的 type error）才对。

所以我猜题主的意思是要充分使用编译器的 type checker 来辅助静态类型推导，而不是 type eraser 或者 reflection 来去猜具体的类型。

以上。
