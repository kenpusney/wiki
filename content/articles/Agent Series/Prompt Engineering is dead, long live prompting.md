让我们再把时间线拨回三年前。

当年我们还在用各种方式分享 Prompt 模板、Stable Diffusion 关键词、最后搞出来 Chain of Thought，然后 Model native reasoning 出现了，一切都不用再麻烦了。

为了接入工作流，最开始我们是用 prompt 来给示例要求输出结构化结果、然后是允许 prompt 一组 schema 让大模型输出结构化结果、然后是 tool use / tool call，然后是 model context protocol 来链接 Chat based 大模型软件和工具，最后完全进展到只通过 Markdown 和少量脚本来实现的 Agent Skill。

为了Feed更多的领域知识，最早我们做的是直接塞进prompt，因为内容量太大于是有了 RAG，再之后是提供工具或者MCP让大模型主动检索，最后变成直接扔一个目录和Playwright （Chrome） MCP 让 Agent 自行去获取信息。

这个系列里我几乎每一篇都在强调**升级对齐定律**，这里就不再特别说了。而我今天想说的是，到底哪些变了，哪些没变。

变了的是上下文——这里并不只是那个8k-1M的token容量，而是模型以及所有能够获取到的输入。
早期的模型能力不足，我们需要 Prompt Engineering 来编排模型能够理解的输入，得到我们预期的输出。而现在reasoning能力都已经是 model native 了，我们需要的操作只是把我们想要的东西告诉目标模型就OK了。

早期的模型context不足，我们需要考虑提供合适的准确的信息就要精细控制上下文中填充的内容，需要 embedding 和 RAG，需要精细设计 tools 的输入输出来优化 token 占用。现在 128k 是入门基础，256k 是大部分主流模型能够做到的，少部分SOTA模型已经能够提供 1M 的context。

早期模型的参数量比较小，后期逐渐提升了训练规模，并且加入了很多针对性的优化，并且扩展了工具调用了agent能力，这种情况下的模型完全能够自动化地去完成相应任务。

早期的应用只有一个单纯的Chat UI，API也只能支持 message 输入，tool use 能力增强以后逐渐出现了功能更加丰富的客户端以及 TUI 的 Agent，除了文本、文件上传和图片以外，这些工具可以直接访问你系统信息、读取文件系统、执行命令和访问网络。

涉及到在线的大模型服务，这方面的能力也都在提升——可以检索网络信息、可以与某些开放的工具交互，然后 会根据你的历史消息记住一些东西——当然这件事情不一定是好事儿，就像我前面提过的，记忆系统现在相当不成熟，哪天你在 Gemini 问过一次脚气怎么治，接下来的聊天里他可能时不时地冒出来关心你的脚气问题。

这是变了的东西——大模型或者Agent的知识储备越来越丰富、获取信息的渠道越来越多、拿到的结果也越来越准确、能够一次性容纳更多的内容来获取更加全面的上下文。

没变的是什么呢？Prompting。

也不是单纯的“Prompt”，而是一套Prompting规则。长期以来我们看Prompt Engineering好像是在如何提供更多的信息给到大模型让他来按照我们的意图生成内容，但其实这个思路一定程度上是反过来的。我们提供的各种信息，更多的是限制大模型不让他过度发散，而是使用我们预期的方式来完成任务——因为现有规模参数量的情况下，我们所能提供到的信息甚至不如它自己编造的丰富，因此让它们按照我们预期的方式来工作的办法就是提供**准确**、**清晰**而且**具体**的规则，让他们按照规则来做事情。

你会发现从 Prompt Engineering 开始我们其实就是在这样做，一直到现在。无论是 AGENTS.md 规范，还是 Agent Skills，还是其他什么花样的操作，其实都是在遵循同样和类似的原则。

说到这儿再插一个题外话，前面我说过记忆系统不靠谱，另外一个不靠谱的东西就是各种抽象技能—— [[Nondeterminism considered harmful]] 之外我本来还想写一个 Abstraction considered harmful 来着，但是现在看很多内容都能在这篇文章里cover了。如果一个Skill写得很抽象，其结果就是起不到任何作用，或者是与预期效果造成严重偏离。

举个例子，我那个编写小说的SKILL并没有什么花哨的东西，就是具体如何构建大纲、角色、和编写小说的指导，也没有任何记忆系统或者所谓的什么抽象思考能力，但是每一篇小说在我这边都有一个严格的标准结构：

```
README.md
STYLEGUIDE.md
00-intake/
01-brief/
02-research/
03-foundation/
  souls/
04-outline/
05-rules/
06-analysis-research/
07-writing/
  samples/
  chapters/
08-operations/
  logs/
  feedback/
  retrospectives/
  change-log/
09-assets/
10-publication/
11-quality/
99-archive/
  samples-YYYYMMDD/
  import-YYYYMMDD/
```

有些人说这就是所谓的Harness Engineering —— 其实归根结底还是Prompting，只是很多东西因为Agent能够识别和理解项目结构，而只要你项目管理能力稍微及格一点就能很好利用这点。
