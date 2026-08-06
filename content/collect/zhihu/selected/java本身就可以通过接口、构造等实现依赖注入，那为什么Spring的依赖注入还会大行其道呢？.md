---
title: java本身就可以通过接口、构造等实现依赖注入，那为什么Spring的依赖注入还会大行其道呢？
date: 2015-12-09
origin: https://www.zhihu.com/question/34967690/answer/75896700
---
# java本身就可以通过接口、构造等实现依赖注入，那为什么Spring的依赖注入还会大行其道呢？

[知乎链接](https://www.zhihu.com/question/34967690/answer/75896700)

---------

请做一个简单对比：
```java
new HelloWorldApp(DefaultStrategyFactory.getInstance(),
        new PrintMessageResolver(
                new TokenizedMessageParser(
                        new WordsTokenizer(DefaultTokenListFactory.getInstance())),
                new ConcreteTokenVisitor()))
        .say(DefaultMessageFactory
                .getInstance().create("Hello world", System.out));

```

和
```java
new ApplicationRunner().run(HelloWorldApp.class);

```

一个用的是手动依赖注入，一个用了IoC容器。

代码见 [kenpusney/hello](https://github.com/kenpusney/hello/)

我觉得很简单，无论是 `@Autowire`，还是xml配置，都需要我做额外的事情就是去读Spring的配置。所以在我的代码里面，`@Inject` 设计成了可以加入实现类的。在 `HelloWorldApp` 里面就能看到他会依赖到哪些东西。当然这也就会带来 Atry 所提到的另外一个问题就是**硬编码**。

但是XML配置和各种 `@Configuration` 依然也是在硬编码嘛。

所以，在程序入口点（比如 `main`）以及各种服务终结点（比如 `routing`），这种硬编码并不需要特别地做额外抽取。这也是为什么第一种做法我依然很喜欢的原因。就像 Atry 说的，所有的依赖一目了然。

诚然，Spring 给了我很多方便的东西，比如 AOP，但这实际上只是在给Java的设计缺陷打补丁。但是反过来看，当国内 Java 社区大部分人都很难驾驭 Scala 的时候，有这么一个补丁也蛮好的。

另外，关于声明式和命令式的问题。我觉得并不是在于是否抽离出一套专门的 DSL（注解也好，XML 配置也好），而是有没有好好考虑过设计。

比如正则表达式，也包含**分支判断**甚至是**断言**，仍不妨碍其精炼的声明式结构。再比如上面代码中的第一种做法，也只是声明并初始化了一个 `HelloWorldApp` 而已。
