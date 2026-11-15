# Phase 1: Hello, LLM

This phase sends your first question to an AI model (an LLM, short for "large language model") from code. Then it looks at what comes back.

## What `hello-llm.py` does

It asks the question *"Explain a Kubernetes pod in one sentence."* to a model running on your own Mac through **Ollama**. Then it prints the answer.

Step by step:

1. **Read settings.** It loads your `.env` file. That's where you can choose a different model or server address.
2. **Pick the model.** It uses `llama3.2:3b` unless you set `OLLAMA_MODEL`.
3. **Start a stopwatch.** This measures how long the model takes to answer.
4. **Send the question.** Ollama runs a small web server on your Mac at `http://localhost:11434`. The script sends the question there and waits for the full answer.
5. **Check for errors.** If something goes wrong (for example, the model isn't downloaded), the script stops with a clear error.
6. **Print the result.** It shows the answer, the tokens in and out, and the time taken.

### What are "tokens"?

Models don't read whole words. They read small pieces called **tokens**, roughly ¾ of a word each.

- **tokens in**: how many tokens your question used
- **tokens out**: how many tokens the answer used

Hosted services like Gemini **charge you per token**, so it helps to get used to these numbers.

Your 10-word question shows up as about 34 input tokens. Ollama adds some hidden text around it, such as "this is the user's message", before the model reads it.

### Example output

```
LOCAL : A Kubernetes pod is a logical hosting unit in a containerized cluster, ...
        tokens in=34 out=46  time=1.6s
```

## How to run it

```bash
# 1. Install Ollama and download the model (one time only)
ollama pull llama3.2:3b

# 2. Run the script from the project root
uv run phase-1/hello-llm.py
```

Optional `.env` settings:

```
OLLAMA_MODEL=llama3.2:3b
OLLAMA_HOST=http://localhost:11434
```

## Local (Ollama) vs hosted (Gemini): what's the difference?

An earlier version of this script asked the same question to **Gemini**, Google's hosted model, too. Here's how the two compare.

| | **Ollama (local, `llama3.2:3b`)** | **Gemini (hosted, Google's servers)** |
|---|---|---|
| **Where it runs** | On your Mac | In Google's data centers |
| **Model size** | Small: 3 billion parameters, about 2 GB | Very large, on powerful hardware |
| **Answer quality** | Fine for simple questions. Gets weaker on hard reasoning, long documents, code, and tricky facts. More likely to make things up. | Much better for complex questions, reasoning, and coding. Knows more and makes fewer mistakes. |
| **Speed on short questions** | Usually fast. No internet trip. | Adds network delay, but Google's hardware generates text very quickly. |
| **Speed on long answers** | Slows down, because your Mac is doing all the work | Stays fast |
| **First call** | Can take several seconds while the model loads into memory. Later calls are faster. | No warm-up on your side |
| **Cost** | Free (you pay in electricity and RAM) | Free tier with limits, then pay per token |
| **Privacy** | Your data never leaves your machine | Your prompt is sent to Google |
| **Internet needed?** | No | Yes |
| **Setup** | Install Ollama and download the model | Need an API key (`GEMINI_API_KEY`) |

### In short

- **Use local (Ollama)** when you want free, private, offline experiments, or simple tasks where "good enough" is fine.
- **Use hosted (Gemini)** when answer quality matters: harder questions, longer text, coding help, or anything users will see.

A common real-world setup uses both: a small local model for cheap or private steps, and a big hosted model for the hard parts.

> **Tip:** To compare them yourself, run the same prompt against both and look at the time and tokens for each. Then read the two answers side by side. Try a harder prompt too, like *"Compare Kubernetes Deployments and StatefulSets with examples."* The quality gap shows up much more clearly on harder questions.
