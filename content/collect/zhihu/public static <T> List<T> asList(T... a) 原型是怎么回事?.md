---
title: public static <T> List<T> asList(T... a) 原型是怎么回事?
date: 2015-07-07
origin: https://www.zhihu.com/question/31967519/answer/54102217
---
# public static <T> List<T> asList(T... a) 原型是怎么回事?

[知乎链接](https://www.zhihu.com/question/31967519/answer/54102217)

---------

泛型的意思是就是说类型可以在以后指定，但是这仍然需要告诉编译器，我需要某个类型作为一个占位符，比如T。
```java
public List<T> fuck(T shit) {
   ...
}
```

然后编译器会问你说，T是个什么鬼？你没有告诉我啊（Cannot resolve symbol）。
所以需要在前面显式地声明一下（这就是为啥不能省略），就成了
```java
public <T> List<T> fuck(T ...) ...
```

共出现了三个T，第一个是用来声明**类型参数**的，后面的两个才是泛型的实现。
所以说Java这种写法丑死了。
看我C#声明和使用多么一致。
```csharp
public List<T> fuck<T>(T shit)
{
   ...
}

```

看我C++，清清楚楚地标明啥是啥。
```cpp
template<typename T>
list<T> fuck(T... shits)
{
   ...
}

```

说起来你要觉得看着像颜文字的话，可以这样写啊：
```java
<Type extends Object> List<Type> fuck(Type... ) ...
```

然而并没有什么用。

以上。
