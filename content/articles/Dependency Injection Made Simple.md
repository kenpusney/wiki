---
title: Dependency Injection made simple
---

假设你在实现一个简单的应用，比如，fizzbuzz。需求非常简单，遇到 3 的倍数，输出 fizz，遇到 5 的倍数，输出 buzz，遇到 3 和 5 的公倍数（common multiple），输出 fizzbuzz。

逻辑非常简单，所以实现起来自然也就很方便。

```js
function fizzbuzz() {
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log("fizzbuzz");
        } else if (i % 3 == 0) {
            console.log("fizz");
        } else if (i % 5 == 0) {
            console.log("buzz");
        }
    }
}
```

但这里我们只说了是输出，并没有说是往什么地方输出，所以这样一来如果需求变成了append到文档末尾而不是输出到控制台，我们就不得不去改fizzbuzz的实现，把三行`console.log`替换成`document.write`。

那更好的办法就是消除重复，我们把console.log这里做一个抽取函数，定义一个专用的print函数专门用来实现输出方式：

```js
function print() {
    // ...
}

function fizzbuzz() {
    for (let i = 1; i <= 100; i ++) {
        if (i % 3 == 0 && i % 5 == 0) {
            print("fizzbuzz");
        } else if (/* ... */)
        // ...
```

这里我们把对console.log的强依赖通过print给屏蔽掉了，但是依然还是保持了对print的强依赖。如此一来fizzbuzz的行为会跟print的具体实现直接相关。如果需求变成了，我需要多个fizzbuzz操作：一种是往控制台输出，一种是往页面追加<del>，另外一种是旋转三周半然后走卫星通讯给火星车发消息告诉可能存在的外星人我们可以进行善意的交流</del>。这个时候现在的fizzbuzz就不太能满足我们的需要了。要解决这个问题，可以选择CV编程法把这段代码复制一份改改函数名完事儿，但这里就又出现了重复。

那如果print这个动作都是可变的，那我们就可以考虑把print做成变量参数化进来，这样每次执行fizzbuzz的时候选择对应的print实现就好了。

```js
function fizzbuzz(printer) {
    for (let i = 1; i <= 100; i ++) {
        if (i % 3 == 0 && i % 5 == 0) {
            printer.print("fizzbuzz");
        } else if (/* ... */)
        // ...
```

其实为了简单你也可以直接传入一个单纯的函数，但稍后我会解释为什么会用这种方法调用的方式。

如此一来，灵活性就有了。fizzbuzz 终于把具体的printer依赖给消除了，变成了每次调用时接受传递进来的依赖。

但是这又导致了另外一个问题。每次我运行fizzbuzz的时候都需要提供一个printer实现。这里对于不希望了解实现细节的调用者来说非常麻烦，甚至还要为了管理printer多做一堆的事情。

比如，如果你无法确定调用者传递进来的printer是不是一个无效值，就得在每次执行的过程中做一些验证，确保printer不会破坏fizzbuzz原本的业务逻辑。

怎么能创造一个保持printer状态的fizzbuzz函数，让我们每次调用的时候都能重复使用一个特定的printer呢？当然是用闭包啦（雾）。

```js
function makeFizzbuzz(printer) {
    // validate printer
    // then
    return function () {
        for (let i = 1; i <= 100; i ++) {
            if (i % 3 == 0 && i % 5 == 0) {
                printer.print("fizzbuzz");
            } else if (/* ... */)
            // ...
    };
}
```

每次makeFizzbuzz得到的都是一个与特定priner绑定的fizzbuzz实现。这样既不失灵活性（因为你可以任意选择printer的实现），又不失易用性（得到的fizzbuzz实现是与printer绑定的，不需要再每次运行都准备一套printer）。

而我们都知道，闭包只是简化了一些的对象。上面这个结构完全可以改成更加自然的没那么隐晦的类/对象结构：

```js
class Fizzbuzz {
    #printer;
    constructor(printer) {
        // validate & bind
        this.#printer = printer;
    }
    run() {
        for (let i = 1; i <= 100; i ++) {
            if (i % 3 == 0 && i % 5 == 0) {
                this.#printer.print("fizzbuzz");
            } else if (/* ... */)
            // ...
    }
}
```

前面我们把print函数替换成printer.print也是基于同样的思路。因为在往火星发消息的时候对于具体发消息的动作也可能存在连接功能或者同步功能等其他形式的依赖，这个时候很难通过一个简单的闭包来构造单纯的函数来做到。所以我们多做了一步事情就是把print也换成了这种类/对象的结构。


回顾一下我们刚才做的所有的事情，

- 首先fizzbuzz强依赖于console.log，通过提取函数的方式我们对这层依赖做了隔离
- 然后fizzbuzz对于print函数的具体实现会有依赖，所以我们通过参数的方式传入printer隔离这一层依赖
- 再之后则是构造期绑定的方式连接fizzbuzz和printer，简化每次运行的时候都要重复传递printer参数这个操作

于是，对于输出操作，或者printer这样一个依赖，我们采用了在构造函数中把它传递进来的方式来处理。这样一来我们就实现了基于构造函数的依赖注入。

## 依赖注入

大多数人把去理解依赖注入都是因为特定的框架，比如知名的Spring Framework。很多人在讲授的过程中一直都会把十几年前EJB时代的老概念拿出来讲一番，然后得出结论说，使用某某框架，你就获得依赖注入了。

然而实际上得到的结果却是，大多数人只记住了依赖注入的三种方式，记住了要分离接口和实现，记住了要用框架/容器。但写出来的代码嘛……

依赖注入框架能够帮到你的只是自动化一部分注入过程，简化你的工作，无法从任何角度指导你设计出来任何好代码。因此，如果你知道自己在干什么，完全可以脱离这些工具然后依然把依赖注入用起来。无非就是把一些操作手动做一遍而已。

我之前就提到过，函数式编程无非就是抽象与组合。实现依赖注入的过程也是一样的。原本简单的逻辑能够实现，然后再通过因为需求膨胀的过程带来的变化抽象成特定的依赖类型，然后把具体依赖的实现组装起来就能得到一个可用的实例。这个过程相对于函数式编程没有那么直观，但包装的无限花哨的各种对象只是类型稍微复杂了一点，组合方式稍微丰富了一点，并且状态稍微多了一点。而因此带来的较之于函数式偏数据流处理的专长，使用依赖注入所组合出来的逻辑可以胜任的工作几乎是无限的。