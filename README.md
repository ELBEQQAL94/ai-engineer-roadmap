# AI Engineer Roadmap: LangChain → LangGraph → Project

## Part 1: LangChain (docs-driven)

### Setup and basics

- [x] Python, virtual environment, and package install
- [x] API keys and `.env` safety, plus spending limits
- [x] Check installed versions against the docs version
- [x] Raw LLM API call (no LangChain) for comparison
- [x] First chat model call with LangChain
- [x] Model parameters: temperature, max tokens
- [x] Switching between providers (OpenAI)
- [x] Note book

### Messages and prompts

- [x] Message types: system, human, AI
- [ ] Prompt templates and chat prompt templates
  - https://docs.langchain.com/langsmith/create-a-prompt
- [ ] Few-shot prompting
- [ ] Streaming responses
- [ ] Batch and async calls

### Structured output

- [ ] Output parsers (string, JSON)
- [ ] Structured output with Pydantic
- [ ] Handling parsing errors and retries

### Runnables and chains (LCEL)

- [ ] What a Runnable is (`invoke`, `stream`, `batch`)
- [ ] Pipe operator and chaining steps
- [ ] `RunnableParallel` and `RunnablePassthrough`
- [ ] `RunnableLambda` (custom functions in a chain)
- [ ] Branching and fallbacks
- [ ] Debugging chains (verbose, callbacks)

### Tools and tool calling

- [ ] Defining tools with the `@tool` decorator
- [ ] Binding tools to a model
- [ ] Executing tool calls and returning results
- [ ] Built-in tools (search, etc.)
- [ ] Tool errors and validation

### Agents (high-level)

- [ ] What an agent is vs. a chain
- [ ] Creating a basic agent with tools
- [ ] Reading agent reasoning steps
- [ ] Limitations that motivate LangGraph

### Memory and conversation history

- [ ] Message history basics
- [ ] Trimming and summarizing long conversations
- [ ] Session-based history

### Retrieval and RAG

- [ ] Document loaders (PDF, web, text)
- [ ] Text splitters and chunking strategies
- [ ] Embeddings
- [ ] Vector stores (Chroma or FAISS)
- [ ] Retrievers and similarity search
- [ ] Building a RAG chain
- [ ] Citing sources in answers
- [ ] Basic RAG evaluation (does it retrieve the right chunks?)

### Observability

- [ ] Tracing with LangSmith (or an alternative)
- [ ] Reading traces to debug

### Part 1 wrap-up

- [ ] Mini project: chat with a PDF
- [ ] Review stream and Q&A

## Part 2: LangGraph

### Core concepts

- [ ] Why LangGraph (limits of chains and simple agents)
- [ ] State: schemas and reducers
- [ ] Nodes and edges
- [ ] Compiling and running a graph
- [ ] Visualizing the graph

### Control flow

- [ ] Conditional edges and routing
- [ ] Loops and cycles
- [ ] Parallel branches
- [ ] Subgraphs

### Agents in LangGraph

- [ ] Building a tool-calling agent from scratch
- [ ] ToolNode and prebuilt components
- [ ] Prebuilt ReAct agent vs. custom graph
- [ ] Error handling and retry logic

### Persistence and control

- [ ] Checkpointers and short-term memory
- [ ] Threads and resuming runs
- [ ] Long-term memory and stores
- [ ] Human-in-the-loop (interrupts and approvals)
- [ ] Time travel and state editing

### Advanced patterns

- [ ] Streaming (tokens, steps, updates)
- [ ] RAG as a graph (adaptive or corrective RAG)
- [ ] Multi-agent patterns (supervisor, handoffs)
- [ ] Debugging and tracing graphs

### Part 2 wrap-up

- [ ] Mini project: multi-step agent
- [ ] Viewer vote on the final project

## Part 3: Final project

### Planning

- [ ] Choose the idea (research agent, document assistant, support bot)
- [ ] Define scope and a minimal version
- [ ] Sketch architecture and graph design
- [ ] Set up repo, README, and folder structure

### Build

- [ ] Core pipeline working end to end
- [ ] Tools and data sources integrated
- [ ] RAG or memory layer added
- [ ] Human-in-the-loop step where it makes sense
- [ ] Error handling and edge cases

### Quality

- [ ] Test with a set of example questions
- [ ] Add tracing and review failures
- [ ] Basic guardrails (input checks, tool limits)
- [ ] Cost and latency review

### Ship

- [ ] Simple UI (Streamlit, Gradio, or FastAPI + frontend)
- [ ] Deploy or package it
- [ ] Write a README with a demo GIF
- [ ] Final showcase stream and lessons learned

## Per-stream checklist (every day)

- [ ] Skim the docs page the night before
- [ ] Recap yesterday, state today's goal
- [ ] Read a section, code it, then modify the example
- [ ] Push code to the repo (`day-XX` folder)
- [ ] Add timestamps and the repo link to the video description
- [ ] Preview tomorrow's topic

## Agent Harness

## Agent problems

- [ ] Deadlock
- [ ] Persistent or fault tolerance

## Deep Agents

## Langsmith

## Agent design pattern

- [] MCP
- [] JEV
