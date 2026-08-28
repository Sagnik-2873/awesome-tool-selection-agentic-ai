# Tools and Libraries

This section collects software frameworks and developer tools that are
useful for building, orchestrating, observing, or evaluating tool-using
and agentic AI systems.

## 1. OpenAI Agents SDK

**Purpose:** A lightweight SDK for building agentic applications with
agents, tools, handoffs, guardrails, sessions, tracing, and MCP tool
integration.

**Why it is relevant:** The SDK provides a practical runtime in which
agents can be equipped with multiple tools and their tool-invocation
behavior can be traced and evaluated.

**Official documentation:** https://platform.openai.com/docs/\
**GitHub:** https://github.com/openai/openai-agents-python

------------------------------------------------------------------------

## 2. LangChain

**Purpose:** An open-source framework for constructing LLM applications
and agents with tools, integrations, retrieval, structured outputs, and
orchestration.

**Why it is relevant:** LangChain provides abstractions for tool calling
and agent execution, making it useful for constructing controlled
multi-tool experiments.

**Official documentation:** https://python.langchain.com/\
**GitHub:** https://github.com/langchain-ai/langchain

------------------------------------------------------------------------

## 3. Microsoft AutoGen

**Purpose:** A framework for developing applications involving AI agents
and multi-agent collaboration.

**Why it is relevant:** AutoGen supports agent-to-agent workflows and
tool-enabled agents, making it useful for studying how agents coordinate
actions and external capabilities.

**Official documentation:** https://microsoft.github.io/autogen/\
**GitHub:** https://github.com/microsoft/autogen

------------------------------------------------------------------------

## 4. LlamaIndex

**Purpose:** A framework for building LLM applications and agents around
data, retrieval, tools, and structured workflows.

**Why it is relevant:** LlamaIndex supports tool-enabled agents and
provides components that can be used to construct retrieval and
tool-selection experiments.

**Official documentation:** https://docs.llamaindex.ai/\
**GitHub:** https://github.com/run-llama/llama_index

------------------------------------------------------------------------

## 5. CrewAI

**Purpose:** A framework for orchestrating role-based AI agents and
workflows with tools and shared task context.

**Why it is relevant:** CrewAI makes it possible to give agents multiple
tools and examine how tool-enabled agents behave within collaborative
workflows.

**Official documentation:** https://docs.crewai.com/\
**GitHub:** https://github.com/crewAIInc/crewAI

------------------------------------------------------------------------

## 6. AgentOps

**Purpose:** An observability and monitoring SDK for AI agents,
including tracing, cost tracking, benchmarking, and integrations with
several agent frameworks.

**Why it is relevant:** Tool-selection research requires detailed
execution traces. Observability systems can capture agent steps, tool
calls, latency, and related runtime information.

**GitHub:** https://github.com/AgentOps-AI/agentops
