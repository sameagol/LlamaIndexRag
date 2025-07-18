from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from .analytics import print_chunk_statistics
import asyncio
import os

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(
    model="llama3.1",
    request_timeout=360.0,
    # Manually set the context window to limit memory usage
    context_window=8000,
)

# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(
    documents,
    # we can optionally override the embed_model here
    # embed_model=Settings.embed_model,
)

print_chunk_statistics(index)

# Allow experimentation with how many similar chunks to retrieve
# via the TOP_K environment variable (5-10 recommended).
top_k = int(os.getenv("TOP_K", "8"))

query_engine = index.as_query_engine(
    # we can optionally override the llm here
    # llm=Settings.llm,
    similarity_top_k=top_k,
    similarity_cutoff=0.75,
)


def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about FAA documents including SAFOs, AIM, and other aviation materials."""
    response = await query_engine.aquery(query)
    return str(response)


# Create an enhanced workflow with both tools
agent = AgentWorkflow.from_tools_or_functions(
    [multiply, search_documents],
    llm=Settings.llm,
    system_prompt="""You are a helpful assistant that can perform calculations
    and search through documents to answer questions.""",
)


# Now we can ask questions about the documents or do calculations
async def main():
    response = await agent.run(
        # "What did the author do in college?"
        "Which FAA SAFOs issued since 2020 focus on runway-incursion prevention, and what common mitigation actions do they recommend to air-carrier operators?"
    )
    print(response)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
