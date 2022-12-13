---
title: 基于形式化验证的注释
date: 2021-07-10
---

这周群里又讨论起来了月经话题了：程序到底该不该加注释。如果你看过我之前的文章，已经把我的观点和理由都充分罗列出来了。

但是毕竟还是无法避免的。我糊玩具编译器的时候反正是不考虑注释，因为没什么用。但是已有的编程语言历史悠久，注释早就是个被玩烂的东西了。而我一直认为最不可容忍的点就是，注释这个玩意儿放在这里是非常影响程序的，因为大部分情况下编译器直接忽略这块儿语法结构，不会对其做验证。这就导致其实我们没办法保证，所写出来的注释就是正确的，更不能保证当代码因为某些逻辑变更改动时，注释也随之更新。

所以如果我们限制一下注释的格式，让他能够变得被形式化验证，不就可以了吗？

正常情况下用自然语言写出来的注释就是可能存在歧义的，但形式化方法发展了这么多年了，各种形形色色的工具都能直接搬进来用。按照这种方式写注释来解释你的代码，远比用绕来绕去说不清楚的自然语言更加高效。反过来还可以根据这些形式化的规范去验证代码实现的正确性，一举两得。

最初我的设想是直接要求在注释里写 TLA+ 这种形式化的建模语言。但是想了想有点不太现实。另外三哥也提出了一个观点，评论必须能够让人直观的看懂，不能有学习成本。但是一方面本身相关结构的命名就能解决这个问题，另外一方面你都在看源码了还不能直观看懂建模工具的spec？

比如下面两个例子：

```js
function sumOfSquares([...array]) {
    let sum = 0;
    for (let item of array) {
        sum += item * item;
    }
    return sum;
}
```

```cpp
float inv_sqrt(float x)
{
    float xhalf = 0.5f*x;
    int i = *(int*)&x;
    i = 0x5f3759df - (i>>1);
    x = *(float*)&i;
    x = x*(1.5f-xhalf*x*x);
    return x;
}
```

虽然相对比较极端，这两个可都不是能够应用注释的地方。第一个直观的就能从函数名看懂一切，第二个就要去读 [Chris Lomont 的 Paper](http://lomont.org/papers/2003/InvSqrt.pdf)才行。其他的场景也几乎一样，要么复杂到你必须有一个相对完善的文档来解释，要么简单到名称解释一切<del>，要么就是写代码的人有问题</del>。

不过既然注释里面写TLA+不是个好选项，那就看下有没有其他的solution吧。不过好在 Java 的生态相对健全的多，很容易就找到了 Java Modeling Language（JML）。

这个工具充分利用了 Java 的注释和 Dijkstra / Hoare 那群人的理论，让你能够在代码里详细的描述清楚自己到底在做什么。并且配合相应的工具能提供编译期甚至运行期的检查。

如下是 OpenJML 官网的一个[示例](http://www.openjml.org/examples/)：

```java
public class BinarySearchGood {
    
    //@ requires sortedArray != null && 0 < sortedArray.length < Integer.MAX_VALUE;
    //@ requires \forall int i; 0 <= i < sortedArray.length; \forall int j; i < j < sortedArray.length; sortedArray[i] <= sortedArray[j];
    //@ old boolean containsValue = (\exists int i; 0 <= i < sortedArray.length; sortedArray[i] == value);
    //@ ensures containsValue <==> 0 <= \result < sortedArray.length;
    //@ ensures !containsValue <==> \result == -1;
    //@ pure
    public static int search(int[] sortedArray, int value) {
        //@ ghost boolean containsValue = (\exists int i; 0 <= i < sortedArray.length; sortedArray[i] == value);
        if (value < sortedArray[0]) return -1;
        if (value > sortedArray[sortedArray.length-1]) return -1;
        int lo = 0;
        int hi = sortedArray.length-1;
        //@ loop_invariant 0 <= lo < sortedArray.length && 0 <= hi < sortedArray.length;
        //@ loop_invariant containsValue ==> sortedArray[lo] <= value <= sortedArray[hi];
        //@ loop_invariant \forall int i; 0 <= i < lo; sortedArray[i] < value;
        //@ loop_invariant \forall int i; hi < i < sortedArray.length; value < sortedArray[i];
        //@ loop_decreases hi - lo;
        while (lo <= hi) {
            int mid = lo + (hi-lo)/2;
            if (sortedArray[mid] == value) {
                return mid;
            } else if (sortedArray[mid] < value) {
                lo = mid+1;
            } else {
                hi = mid-1;
            }
        }
        return -1;
    }
}
```

虽然这一堆的 `requires` `ensures` 和 `invariant` 让人觉得真不如直接上 Eiffel（或者其他有 Design by Contract 构造的编程语言），但是这是在Java里面，并且

- 可检查
- 容易理解
- 100% 兼容现有的Java（虽然只支持 JDK 8）语法

当然问题就是写起来真的太难了。

不过我觉得这也是个好事儿，如果我们在Lint规则里面禁用除了 JML 以外的其他所有注释，这样就正如熊节老师说的，这样注释比代码更难写，也就能改掉那些人的诡异习惯了。
