
# Building effective agents


Published Dec 19, 2024 [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

## What are agents?

At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

## When (and when not) to use agents

Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale.

## When and how to use frameworks

If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

## Building blocks, workflows, and agents

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory.

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one.

You can add programmatic checks on any intermediate steps to ensure that the process is still on track.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

**When to use this workflow:** Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results.

### Workflow: Orchestrator-workers

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

**When to use this workflow:** This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task).

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors.

Agents can handle sophisticated tasks, but their implementation is often straightforward.

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path.

## Combining and customizing these patterns

 You should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent's planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production.

# Memory & context management with Claude Sonnet 4.6

Published on May 22, 2025 [Memory & context management with Claude Sonnet 4.6](https://platform.claude.com/cookbook/tool-use-memory-cookbook)

### The Problem

Large language models have finite context windows (200k tokens for Claude 4). While this seems large, several challenges emerge:

- **Context limits**: Long conversations or complex tasks can exceed available context
- **Computational cost**: Processing large contexts is expensive - attention mechanisms scale quadratically
- **Repeated patterns**: Similar tasks across conversations require re-explaining context every time
- **Information loss**: When context fills up, earlier important information gets lost

##  Use Cases

Memory and context management enable powerful new workflows:

### 🔍 Code Review Assistant

- Learns debugging patterns from past reviews
- Recognizes similar bugs instantly in future sessions
- Builds team-specific code quality knowledge
- **Production ready**: Integrate with [claude-code-action](https://github.com/anthropics/claude-code-action) for GitHub PR reviews

### 📚 Research Assistant

- Accumulates knowledge on topics over multiple sessions
- Connects insights across different research threads
- Maintains bibliography and source tracking

### 💬 Customer Support Bot

- Learns user preferences and communication style
- Remembers common issues and solutions
- Builds product knowledge base from interactions

### 📊 Data Analysis Helper

- Remembers dataset patterns and anomalies
- Stores analysis techniques that work well
- Builds domain-specific insights over time

**⚠️ Note on Memory Clearing**

**In production applications**, you should carefully consider whether to clear all memory, as it permanently removes learned patterns. Consider using selective deletion or organizing memory into project-specific directories instead.

## Best Practices & Security

### Memory Management

**Do:**

- ✅ Store task-relevant patterns, not conversation history
- ✅ Organize with clear directory structure
- ✅ Use descriptive file names
- ✅ Periodically review and clean up memory

**Don't:**

- ❌ Store sensitive information (passwords, API keys, PII)
- ❌ Let memory grow unbounded
- ❌ Store everything indiscriminately

### Security: Path Traversal Protection

**Critical**: Always validate paths to prevent directory traversal attacks. See `memory_tool.py` for implementation.

### Security: Memory Poisoning

**⚠️ Critical Risk**: Memory files are read back into Claude's context, making them a potential vector for prompt injection.

**Mitigation strategies:**

1. **Content Sanitization**: Filter dangerous patterns before storing
2. **Memory Scope Isolation**: Per-user/per-project isolation
3. **Memory Auditing**: Log and scan all memory operations
4. **Prompt Engineering**: Instruct Claude to ignore instructions in memory




# How we built our multi-agent research system

Published Jun 13, 2025 [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

### Prompt engineering and evaluations for research agents

- **Think like your agents.** Effective prompting relies on developing an accurate mental model of the agent, which can make the most impactful changes obvious.
- **Teach the orchestrator how to delegate.** Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information.
- **Scale effort to query complexity.** Agents struggle to judge appropriate effort for different tasks, so we embedded scaling rules in the prompts.
- **Tool design and selection are critical.** Agent-tool interfaces are as critical as human-computer interfaces. Using the right tool is efficient—often, it's strictly necessary. Bad tool descriptions can send agents down completely wrong paths, so each tool needs a distinct purpose and a clear description.
- **Let agents improve themselves**. When given a prompt and a failure mode, they are able to diagnose why the agent is failing and suggest improvements.
- **Start wide, then narrow down.** Search strategy should mirror expert human research: explore the landscape before drilling into specifics. Agents often default to overly long, specific queries that return few results.
- **Guide the thinking process.** This makes subagents more effective in adapting to any task.
- **Parallel tool calling transforms speed and performance.**

### Effective evaluation of agents

- **Start evaluating immediately with small samples**.
- **LLM-as-judge evaluation scales when done well.** Using an LLM as a judge allowed us to scalably evaluate hundreds of outputs.
- **Human evaluation catches what automation misses.**

### Production reliability and engineering challenges

- **Agents are stateful and errors compound.**
- **Debugging benefits from new approaches.**
- **Deployment needs careful coordination.**
- **Synchronous execution creates bottlenecks.**

## Appendix

- **End-state evaluation of agents that mutate state over many turns.**
- **Long-horizon conversation management.** Production agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies. As conversations extend, standard context windows become insufficient, necessitating intelligent compression and memory mechanisms. We implemented patterns where agents summarize completed work phases and store essential information in external memory before proceeding to new tasks. When context limits approach, agents can spawn fresh subagents with clean contexts while maintaining continuity through careful handoffs. Further, they can retrieve stored context like the research plan from their memory rather than losing previous work when reaching the context limit.
- **Subagent output to a filesystem to minimize the 'game of telephone.'**




# Writing effective tools for agents — with agents

Published Sep 11, 2025 [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

> Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.

In computing, deterministic systems produce the same output every time given identical inputs, while _non-deterministic_ systems—like agents—can generate varied responses even with the same starting conditions.

Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents.

## How to write tools

- Building a prototype
- Running an evaluation
	- **Generating evaluation tasks**
	- **Running the evaluation**
	- **Analyzing results**
- Collaborating with agents

## Principles for writing effective tools

### Choosing the right tools for agents

More tools don't always lead to better outcomes. Agents have distinct "affordances" to traditional software—that is, they have different ways of perceiving the potential actions they can take with those tools.

Building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there.

Tools can consolidate functionality, handling potentially _multiple_ discrete operations (or API calls) under the hood.

Make sure each tool you build has a clear, distinct purpose.

Too many tools or overlapping tools can also distract agents from pursuing efficient strategies.

### Namespacing your tools

Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools.

By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent's context and offload agentic computation from the agent's context back into the tool calls themselves.

### Returning meaningful context from your tools

Tool result should prioritize contextual relevance over flexibility.

Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers.

In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls. You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `“concise”` or `“detailed”` responses (images below).

We encourage you to select the best response structure based on your own evaluation.
### Optimizing tool responses for token efficiency

We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context.

If you choose to truncate responses, be sure to steer agents with helpful instructions.

Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

### Prompt-engineering your tool descriptions

When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team.

Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit.

Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.

With your evaluation you can measure the impact of your prompt engineering with greater confidence.

> [!info]- Refs: Define Tools Best Practices
>  
>  ### Best practices for tool definitions
>  
> To get the best performance out of Claude when using tools, follow these guidelines:
> 
> - **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:
>     - What the tool does
>     - When it should be used (and when it shouldn't)
>     - What each parameter means and how it affects the tool's behavior
>     - Any important caveats or limitations, such as what information the tool does not return if the tool name is unclear. The more context you can give Claude about your tools, the better it will be at deciding when and how to use them. Aim for at least 3–4 sentences for each tool description, more if the tool is complex.
> - **Prioritize descriptions, but consider using `input_examples` for complex tools.** Clear descriptions are most important, but for tools with complex inputs, nested objects, or format-sensitive parameters, you can use the `input_examples` field to provide schema-validated examples. See [Providing tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples) for details.
> - **Consolidate related operations into fewer tools.** Rather than creating a separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and make your tool surface easier for Claude to navigate.
> - **Use meaningful namespacing in tool names.** When your tools span multiple services or resources, prefix names with the service (for example, `github_list_prs`, `slack_send_message`). This makes tool selection unambiguous as your library grows, and is especially important when using [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool).
> - **Design tool responses to return only high-signal information.** Return semantic, stable identifiers (for example, slugs or UUIDs) rather than opaque internal references, and include only the fields Claude needs to reason about its next step. Bloated responses waste context and make it harder for Claude to extract what matters.
>
> ## Providing tool use examples
> 
> You can provide concrete examples of valid tool inputs to help Claude understand how to use your tools more effectively. This is particularly useful for complex tools with nested objects, optional parameters, or format-sensitive inputs.
> 
> Examples are included in the prompt alongside your tool schema, showing Claude concrete patterns for well-formed tool calls. This helps Claude understand when to include optional parameters, what formats to use, and how to structure complex inputs.
> 
> ### Requirements and limitations
>
> - **Schema validation** - Each example must be valid according to the tool's `input_schema`. Invalid examples return a 400 error
> - **Not supported for server-side tools** - Input examples work on user-defined and Anthropic-schema client tools, but not on server tools such as web search or code execution
> - **Token cost** - Examples add to prompt tokens: ~20–50 tokens for simple examples, ~100–200 tokens for complex nested objects


# Effective context engineering for AI agents

Published Sep 29, 2025 [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

**Context** refers to the set of tokens included when sampling from a large-language model (LLM).

**Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information.

> [!info]- [Karpathy's Tweet](https://x.com/karpathy/status/1937902205765607626)
> +1 for "context engineering" over "prompt engineering". 
> 
> People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step. Science because doing this right involves task descriptions and explanations, few shot examples, RAG, related (possibly multimodal) data, tools, state and history, compacting... Too little or of the wrong form and the LLM doesn't have the right context for optimal performance. Too much or too irrelevant and the LLM costs might go up and performance might come down. Doing this well is highly non-trivial. And art because of the guiding intuition around LLM psychology of people spirits.
> 
> On top of context engineering itself, an LLM app has to:
>  - break up problems just right into control flows
>  - pack the context windows just right
>  - dispatch calls to LLMs of the right kind and capability
>  - handle generation-verification UIUX flows
>  - a lot more - guardrails, security, evals, parallelism, prefetching, ... 
>  
>  So context engineering is just one small piece of an emerging thick layer of non-trivial software that coordinates individual LLM calls (and a lot more) into full LLM apps. The term "ChatGPT wrapper" is tired and really, really wrong.

[Context Rot](https://www.trychroma.com/research/context-rot) issue: As the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases.

## The anatomy of effective context

**System prompts** should be extremely clear and use simple, direct language that presents ideas at the _right altitude_ for the agent.
- organizing prompts into distinct sections
- using format to delineate these sections
- striving for the minimal set of information
	- (minimal does not necessarily mean short)
	- best to start by testing a minimal prompt with the best model available to see how it performs on your task, and then add clear instructions and examples to improve performance based on failure modes found during initial testing

**Tools** allow agents to operate with their environment and pull in new, additional context as they work

-  minimal overlap in functionality

> If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better.

Curating a minimal viable set of tools for the agent can also lead to more reliable maintenance and pruning of context over long interactions.

Providing examples - curate a set of diverse, canonical examples that effectively portray the expected behavior of the agent.

## Context retrieval and agentic search

> Agents are LLMs autonomously using tools in a loop.

dynamically load data into context at runtime using tools instead of pre-processing all relevant data up front.

Beyond storage efficiency, the metadata of these references provides a mechanism to efficiently refine behavior, whether explicitly provided or intuitive. Naming conventions, and timestamps all provide important signals that help both humans and agents understand how and when to utilize information

Letting agents navigate and retrieve data autonomously also enables progressive disclosure.

Trade-off: runtime exploration is slower than retrieving pre-computed data.

### Context engineering for long-horizon tasks

- Compaction
- Structured note-taking
- Sub-agents

The choice between these approaches depends on task characteristics. For example:

- Compaction maintains conversational flow for tasks requiring extensive back-and-forth;
- Note-taking excels for iterative development with clear milestones;
- Multi-agent architectures handle complex research and analysis where parallel exploration pays dividends.






# Effective harnesses for long-running agents

Published Nov 26, 2025 [Effective harness for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

> Agents still face challenges working across many context windows. We looked to human engineers for inspiration in creating a more effective harness for long-running agents.

The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before.

We developed a two-fold solution to enable the [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) to work effectively across many context windows: an **initializer agent** that sets up the environment on the first run, and a **coding agent** that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session.

## The long-running agent problem

- First, the agent tended to try to do too much at once—essentially to attempt to one-shot the app.
- A second failure mode would often occur later in a project. After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done.

When experimenting internally, we addressed these problems using a two-part solution:

1. Initializer agent: The very first agent session uses a specialized prompt that asks the model to set up the initial environment: an `init.sh` script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit that shows what files were added.
2. Coding agent: Every subsequent session asks the model to make incremental progress, then leave structured updates.1

## Environment management

### Feature list

### Incremental progress

work on only one feature at a time.

### Testing

One final major failure mode that we observed was Claude’s tendency to mark a feature as complete without proper testing.

> [!info] Agent failure modes and solutions
> 
> |**Problem**|**Initializer Agent Behavior**|**Coding Agent Behavior**|
> |---|---|---|
> |Claude declares victory on the entire project too early.|Set up a feature list file: based on the input spec, set up a structured JSON file with a list of end-to-end feature descriptions.|Read the feature list file at the beginning of a session. Choose a single feature to start working on.|
> |Claude leaves the environment in a state with bugs or undocumented progress.|An initial git repo and progress notes file is written.|Start the session by reading the progress notes file and git commit logs, and run a basic test on the development server to catch any undocumented bugs. End the session by writing a git commit and progress update.|
> |Claude marks features as done prematurely.|Set up a feature list file.|Self-verify all features. Only mark features as “passing” after careful testing.|
> |Claude has to spend time figuring out how to run the app.|Write an `init.sh` script that can run the development server.|Start the session by reading `init.sh`.|




