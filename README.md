# LlamaIndex RAG Example

This repository contains a minimal example for building a Retrieval-Augmented Generation (RAG) workflow with [LlamaIndex](https://github.com/run-llama/llama_index).

The `starter.py` script follows the official [starter example](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/) from the docs. It loads text files from the `data/` directory, creates an index and runs a sample query using a model served by [Ollama](https://ollama.com/).

The script now also prints statistics about how the index was created. Each
chunk's statistics include a short snippet from the original text so you can see
what content ended up in the index.

## Setup

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Ensure [Ollama](https://ollama.com/) is installed and running locally.
   If needed, pull a model and start the server:

```bash
ollama pull llama3
```

3. Run the script (set `TOP_K` to change how many chunks to search)

```bash
TOP_K=8 python starter.py
```

4. Download the AIM Basic PDF

```bash
python src/download_aim.py
```

5. Download SAFO PDFs

```bash
python src/download_safo.py
```

6. Parse PDFs using the smart loader

```bash
python -c "from src import load_pdfs; print(len(load_pdfs(['data/aim_basic.pdf'])))"
```
