# LlamaIndex RAG Example

This repository contains a minimal example for building a Retrieval-Augmented Generation (RAG) workflow with [LlamaIndex](https://github.com/run-llama/llama_index).

The `starter.py` script follows the official [starter example](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/) from the docs. It loads text files from the `data/` directory, creates an index and runs a sample query using your OpenAI API key.

## Setup

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key and run the script

```bash
export OPENAI_API_KEY=sk-...
python starter.py
```

Replace `sk-...` with your actual API key.
