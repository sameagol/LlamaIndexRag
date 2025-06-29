# LlamaIndex RAG Example

This repository contains a minimal example for building a Retrieval-Augmented Generation (RAG) workflow with [LlamaIndex](https://github.com/run-llama/llama_index).

The `starter.py` script loads text files from the `data/` directory, builds an index and then runs a small agent workflow powered by a model served by [Ollama](https://ollama.com/). The agent can answer questions about the documents and perform simple calculations.

## Setup

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Ensure [Ollama](https://ollama.com/) is installed and running locally.
   If needed, pull a model and start the server:

```bash
ollama pull llama3
ollama serve
```

3. Run the script

```bash
python starter.py
```
