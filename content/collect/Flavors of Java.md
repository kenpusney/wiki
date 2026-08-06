
我想当场的工作时间使用的语言都是Java，这里列举一些我推荐（以及不推荐的）工具库，和他们之间的对比。

## 通用框架

- [Dagger](https://dagger.dev) （Google 开源的一款编译期依赖注入框架）
	- 其他可选的有 Google Guice、Spring （老牌）
	- Dagger的优势是编译期依赖注入，这意味着你可以在编译构建的时候就检查到组件的差异，同时也可以在这一层就把不同层级的模块组装起来，而实现依然分散在不同的module里，在结合了诸如 Bazel 等构建工具以后，很容易组合成一个庞大的monorepo。至今我的Java仓库还是这么一个整体。
	- Guice 相对太简单了，不过作为一个轻量工具也确实值得一试。
	- Spring 嘛，用了就意味着你要绑定整个生态，恨不得什么东西都离不开 Boot 那一套，毕竟社区主流，更适合直接上一整套解决方案用。当然带来的另一个问题就是太庞大了，任何问题都能复杂化成一堆的解决方案。
	- 另外一个问题就是隐式操作太多了。Explicit is better than implicit.

## Data Access

- [JDBI](http://jdbi.org/)
	- 比起纯粹的 Spring JDBC Template 要强不少，有相对自动的绑定功能。
	- 比起纯粹的query mapper，灵活性又能高到像JDBC Template那样。
	- 类似 Spring Data JDBC，但是不需要 Spring Data 那一套复杂的东西。
	- 至于 MyBatis 这种奇怪的框架，以及再之上的各种封装……我觉得纯粹是硬造出来的需求
	- 至于 JPA，可以理解，但这是上个时代的需求了
- Lettuce vs Redisson vs Jedis
	- 完全看心情。Redisson 更像是个分布式的框架，很多数据结构也都分布式化了。
	- Jedis 和 Lettuce则是看是否需要异步操作。
- Jackson
	- 简单直观。ObjectMapper用来做转换，Annotations用来定义Schema。加上其他的一些组件，直观地把数据序列化反序列化给呈现得很清晰。
	- Gson有点诡异，很多东西设计的如同其他Google库一样奇怪，Google的口味难以理解。
		- Guava也是一堆奇形怪状口味的设计
		- 好在口碑还在，作为一个轻量级的工具基本还可用
	- FastJSON真就是垃圾中的垃圾了
- Binary Format
	- Hessian 这种奇怪的东西我都不知道怎么会流行起来的，Dubbo这垃圾影响了不知道多少所谓的中台业务，太臭了。
	- Kyro好像是另一个Java native的二进制序列化库，没尝试过。
	- Google Protobuf有跟其他Google库同样的问题，另外，需要protoc这个过程是非常麻烦的。好在protobuf对于不同版本的结构是兼容的。
	- Msgpack 相当轻量级，alternative to JSON，是个很不错的选择，简单用的话问题不大
	- Thrift我觉得只能用在他RPC那一层，而且跟上面大部分一样都不是Java Native，意味着需要一层 IDL，问题很大
- Schema Migration
	- Redgate Flyway
	- Liquibase
## 测试

- JUnit
	- 简单纯粹，好用
	- 另外两个JVM生态我感觉可用的是 [Spek](https://www.spekframework.org/) 和 [Spock](https://spockframework.org/)
	- Spock的 GWT DSL 简直太好用了
- Mockito
	- 比 Easymock 更加 DSL 话
	- 比 Powermock 更简单
		- 一旦用到了 Powermock，就意味着你需要重新设计了
		- 比如需要 Mock private / static 方法，这都是很奇怪的设计
	- 有些地方行为可能会很奇怪
- AssertJ
	- JUnit自带的Assertion并非不好用，但是相对来说不够fluent。
	- JUnit 4和Hamcrest matchers组合起来看起来不错，但是又是legacy的东西了
	- AssertJ这一步插入进来的感觉就非常不错
	
## IO / Asynchronous / Reactive

- Netty
- Project Reactor
- RxJava

## Utils

- Logging
	- Slf4j + Logback
- Bean Definition
	- Immutables
	- Lombok
