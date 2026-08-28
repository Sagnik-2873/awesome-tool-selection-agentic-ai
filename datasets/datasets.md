# Datasets and Benchmarks

This collection highlights datasets and benchmarks that can be used to
study tool selection, tool calling, agent planning, multi-step
execution, and agent reliability.

## 1. API-Bank

**Paper:** Li et al., *API-Bank: A Comprehensive Benchmark for
Tool-Augmented LLMs* (2023)

**What it provides:** An executable benchmark for evaluating language
models on API/tool retrieval, planning, and calling.

**Why it matters for tool selection:** API-Bank separates the problem of
deciding how to use external APIs from ordinary question answering and
therefore provides a direct basis for studying tool-selection and
tool-execution accuracy.

**Scholarly source:** https://aclanthology.org/2023.emnlp-main.187/

------------------------------------------------------------------------

## 2. ToolBench

**Paper:** Qin et al., *ToolBench: Towards Mastering Every Tool for
LLMs* (2023/2024)

**What it provides:** A large-scale collection and evaluation
environment built around thousands of real-world APIs.

**Why it matters for tool selection:** ToolBench supports research on
retrieving relevant tools from large collections, planning API calls,
and executing multi-step tool-use tasks.

**Scholarly source:** https://arxiv.org/abs/2307.16789

------------------------------------------------------------------------

## 3. AgentBench

**Paper:** Liu et al., *AgentBench: Evaluating LLMs as Agents* (2023)

**What it provides:** A multi-dimensional benchmark covering LLM agents
in several interactive environments.

**Why it matters for tool selection:** It evaluates agents through
interaction rather than only static question answering, making it useful
for studying action selection, planning, and task completion.

**Scholarly source:** https://arxiv.org/abs/2308.03688

------------------------------------------------------------------------

## 4. WebArena

**Paper:** Zhou et al., *WebArena: A Realistic Web Environment for
Building Autonomous Agents* (2023)

**What it provides:** Realistic, self-hostable web environments in which
agents perform long-horizon tasks.

**Why it matters for tool selection:** Web tasks require agents to
choose appropriate actions and interact with multiple external
interfaces over several steps.

**Scholarly source:** https://arxiv.org/abs/2307.13854

------------------------------------------------------------------------

## 5. τ-bench

**Paper:** Yao et al., *τ-bench: A Benchmark for Tool-Agent-User
Interaction in Real-World Domains* (2024)

**What it provides:** A benchmark for agents interacting with both users
and domain-specific tools under explicit policies.

**Why it matters for tool selection:** It measures whether agents can
select and use tools correctly while maintaining policy compliance and
handling multi-turn interaction.

**Scholarly source:** https://arxiv.org/abs/2406.12045

------------------------------------------------------------------------

## 6. ToolQA

**Paper:** Zhuang et al., *ToolQA: A Dataset for LLM Question Answering
with External Tools* (2023)

**What it provides:** Questions requiring external tools and knowledge
sources to obtain answers.

**Why it matters for tool selection:** ToolQA tests whether models
recognize when external tools are necessary and can use them to solve
tasks.

**Scholarly source:** https://arxiv.org/abs/2306.13304

------------------------------------------------------------------------

## 7. ToolSandbox

**Paper:** Lu et al., *ToolSandbox: A Stateful, Conversational,
Interactive Evaluation Benchmark for LLM Tool Use Capabilities* (2025)

**What it provides:** Stateful and conversational tool-use environments
with evaluation of intermediate and final outcomes.

**Why it matters for tool selection:** It supports trajectory-level
analysis, which is important when tool selection must be evaluated at
every step rather than only from the final answer.

**Scholarly source:** https://aclanthology.org/2025.findings-naacl.65/

------------------------------------------------------------------------

## 8. Live API-Bench

**Paper:** Elder et al., *Live API-Bench: 2500+ Live APIs for Testing
Multi-Step Tool Calling* (2026)

**What it provides:** A large benchmark based on more than 2,500 live
APIs and multi-step tool-calling tasks.

**Why it matters for tool selection:** It directly addresses large tool
inventories and multi-step tool calling, allowing evaluation of
selection, ordering, and argument correctness.

**Scholarly source:** https://aclanthology.org/2026.eacl-long.143/

------------------------------------------------------------------------

## Recommended Evaluation Dimensions

For this repository's research topic, benchmark results should ideally
be analyzed using more than final task success:

-   **Tool-selection accuracy:** whether the correct tool was selected.
-   **Tool necessity accuracy:** whether the agent correctly decided to
    use or not use a tool.
-   **Argument accuracy:** whether the selected tool received valid
    arguments.
-   **Tool-order accuracy:** whether tools were selected in a valid
    sequence.
-   **Execution success:** whether the selected tool calls actually
    succeeded.
-   **Trajectory success:** whether the complete sequence of decisions
    solved the task.
-   **Cost and latency:** whether selection quality was achieved
    efficiently.
-   **Robustness:** whether the agent behaves consistently across
    repeated runs or tool perturbations.
