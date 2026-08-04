---
title: 现在最常用的Java消息队列中间件是哪个？
date: 2015-10-30
origin: https://www.zhihu.com/question/37014051/answer/70007637
---
# 现在最常用的Java消息队列中间件是哪个？

[知乎链接](https://www.zhihu.com/question/37014051/answer/70007637)

---------

只说开源的。

作为经典的MOM，ActiveMQ还是在企业应用中出场率很高的。
HornetQ跟JBoss绑定在一起，应用也很普遍。
毕竟JMS是业界标准。

不过如果你想尝鲜，也可以玩一玩Kafka。

另推荐：[http://www.predic8.com/activemq-hornetq-rabbitmq-apollo-qpid-comparison.htm](http://www.predic8.com/activemq-hornetq-rabbitmq-apollo-qpid-comparison.htm)
毕竟不是说Java应用的所有组件和依赖都要用Java实现。所以你可以去了解下RabbitMQ / ZeroMQ / Disque etc.
