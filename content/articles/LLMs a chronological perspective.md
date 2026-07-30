## Terms
- `LLM: Large Language Model`. Why `Large`.
- Traditional language models:
	- Specific tasks
		- Classification
		- Summarization
		- Translation
		- Feature extraction
- Large:
	- General purpose
	- Pre-trained on large corpora
	- Fine-tuned for specific tasks
## Pre-LLM era
- 1950s: Alan Turing's "Computing Machinery and Intelligence" (1950)
- 1980s: Statistical language models (e.g., n-grams)
- 1990s: Neural networks for NLP (e.g., Elman networks)
- 2000s: Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks
- 2010s: Attention mechanisms and Transformers
- Mixture of Experts (MoE):
	- 2017: "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer" (Shazeer et al., Google)
- `BERT` (2018) by Google:
	- Bidirectional Encoder Representations from Transformers
- `GPT` (2018) by OpenAI:
	- Generative Pre-trained Transformer
## LLM era
- 2020: GPT-3 (175 billion parameters)

## Prompting
- Few-shot learning:
	- 2020: "Language Models are Few-Shot Learners" (Brown et al., OpenAI)

## Fine-tuning
- Low-Rank Adaptation (LoRA) (2021)
- Parameter-efficient fine-tuning (PEFT)

## RAG
- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG) (2020)

## Instruction-following LLMs
- 2022: InstructGPT (OpenAI)
- 2023: ChatGPT (OpenAI)

## Prompt Chaining
- 2022: "Chain of Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., Google)
- 2023: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models" (Zhou et al., Google)
- PromptChainer: Chaining Large Language Model Prompts through Visual Programming
### Model-native Reasoning
- OpenAI introduced this terminology in September 2024 when it released the o1 series, describing the models as designed to "spend more time thinking" before responding. The company framed o1 as a reset in model naming that targets complex tasks in science, coding, and mathematics, and it contrasted o1's performance with GPT-4o on benchmarks such as AIME and Codeforces. Independent reporting the same week summarized the launch and highlighted OpenAI's claim that o1 automates chain-of-thought style reasoning to achieve large gains on difficult exams.
- "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (2024, DeepSeek)

## Agency
- 2022: "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., Google)
- 2023: Describe, Explain, Plan and Select: Interactive Planning with LLMs Enables Open-World Multi-Task Agents

## Tool use
- 2023: "Toolformer: Language Models Can Teach Themselves to Use Tools" (Meta AI)
- Gorilla: Large Language Model Connected with Massive APIs (UC Berkeley, Microsoft, 2023)

## Model Context Protocol
- Anthropic 2024

## Agent Skills
- 2025 Oct. Anthropic

## One more thing
- ### Open Source LLMs
	- GPT-Neo (EleutherAI) 2021
	- LLaMA (Meta) 2023
	- Mistral (2023) 7B and 8B models
	- Qwen (Alibaba) 2023
	- Baichuan (Baidu) 2023
	- Gemma (Google) 2023
- ### Framework & Runtime
	- Pytorch
	- #### Runtime
		- OnnxRuntime - 微软
		- TensorRT、LiteRT、JAX - Google
		- llama.cpp
		- MLX - Apple
		- vLLM
		- SGLang