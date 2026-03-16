# 🧠 AgentAll — Modular ReAct AI Agent Framework

A modular **LLM-powered AI Agent framework** built in Python that follows the **ReAct (Reason + Act)** paradigm.

The agent can:

- Reason step-by-step
- Use external tools (web search, webpage extraction)
- Maintain conversational context
- Store short-term and long-term memory
- Dynamically decide when to search, extract, or answer

The architecture is designed to resemble **modern research agents** used in systems like **Perplexity, OpenAI Deep Research, and AutoGPT-style planners**, while remaining lightweight and fully local.

---

# 🚀 Key Features

### 🔹 ReAct Reasoning Loop
The agent follows a structured reasoning loop:

```
Thought → Tool Call → Observation → Thought → Final Answer
```

This allows the model to:

- Plan information gathering
- Use tools when needed
- Update reasoning based on tool results
- Produce grounded answers

---

### 🔹 External Tool Integration

Currently supported tools:

| Tool | Description |
|-----|-------------|
| `web_search` | Searches the internet using Tavily |
| `web_extract` | Extracts relevant content from webpages |

The agent decides **when tools are required** rather than blindly calling them.

---

### 🔹 Context Management

The system maintains conversational state through a **context manager** which:

- Stores user messages
- Stores assistant responses
- Injects tool observations
- Builds the final prompt for the LLM

This ensures the model always has **relevant conversation history**.

---

### 🔹 Memory System

The framework supports **multi-layer memory**:

| Memory Type | Purpose |
|-------------|--------|
| Short-term memory | Recent conversation context |
| Summary memory | Compressed history of older chats |
| Profile memory | Persistent user information |

Example stored data:

```
storage/profile.json
storage/chat_summary.txt
```

---

### 🔹 Tool Execution Engine

Tools are executed asynchronously through the **tool executor** which:

- Handles parallel execution
- Formats tool results
- Compresses large outputs
- Converts tool responses into structured observations

This allows the agent to **reason over tool outputs efficiently**.

---

# 🏗️ Project Architecture

```
agent/
│
├── brain/
│   ├── phi_client.py        # Main LLM interface
│   └── utility_llm.py       # Smaller utility model
│
├── context/
│   └── context_manager.py   # Conversation state manager
│
├── core/
│   ├── agent.py             # Main agent interface
│   ├── react_loop.py        # ReAct reasoning loop
│   ├── planner.py           # Planning module
│   ├── executor.py          # Task execution
│   ├── tool_executor.py     # Async tool execution
│   ├── tool_registry.py     # Tool registration system
│   ├── prompt_builder.py    # Builds final LLM prompts
│   └── agent_response.py    # Parses LLM JSON responses
│
├── memory/
│   ├── memory_manager.py
│   ├── short_term.py
│   ├── summary_memory.py
│   └── profile_memory.py
│
├── tools/
│   ├── base_tool.py
│   └── tavily_search.py
│
├── prompts/
│   └── system prompts
│
├── storage/
│   ├── profile.json
│   └── chat_summary.txt
│
├── main.py                  # Entry point
└── .env                     # API keys
```

---

# ⚙️ How The Agent Works

### Step 1 — User Query

The user sends a question:

```
User → Agent
```

---

### Step 2 — Prompt Construction

The system builds a prompt containing:

- System instructions
- Available tools
- Conversation history
- Tool usage state

---

### Step 3 — LLM Reasoning

The model returns a structured JSON response:

```json
{
  "thought": "...",
  "tool_calls": [...],
  "final_answer": null
}
```

---

### Step 4 — Tool Execution

If tools are requested:

```
Agent → Tool Executor → External API
```

Tool results are converted into **OBSERVATION blocks**.

---

### Step 5 — Iterative Reasoning

The agent continues the loop:

```
Thought → Tool → Observation
```

until it produces:

```
final_answer
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/agentall.git
cd agentall
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```
TAVILY_API_KEY=your_api_key_here
```

You can get a key from:

https://tavily.com

---

# ▶️ Running the Agent

Start the agent:

```bash
python main.py
```

Example usage:

```
You: what is quantum computing?

Agent:
<thinks, searches web, extracts data>
Final Answer...
```

---

# 🧩 Extending the Agent

Adding a new tool requires three steps:

### 1️⃣ Create the tool

```
tools/my_tool.py
```

---

### 2️⃣ Register the tool

```
core/tool_registry.py
```

---

### 3️⃣ Update prompt documentation

Add the tool description so the LLM knows how to use it.

---

# 🛠 Future Improvements

Planned improvements include:

- Semantic search memory
- Tool result ranking
- Page chunking for large documents
- Multi-tool parallel reasoning
- Local embedding retrieval
- Autonomous planning agents

---

# 📚 Inspiration

This framework is inspired by research and systems such as:

- ReAct (Reason + Act prompting)
- OpenAI Tool Agents
- AutoGPT
- Perplexity AI research agents
- LangChain agent frameworks

---

# 👨‍💻 Author

**Vijay Khantwal**

AI agent experimentation and LLM systems engineering.

---

# 📜 License

MIT License
