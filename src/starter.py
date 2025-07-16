"""Example script for querying a persisted index."""

import asyncio
import os

from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core import Settings
from .analytics import print_chunk_statistics
from .index_utils import (
    DEFAULT_DATA_DIR,
    DEFAULT_PERSIST_DIR,
    load_or_create_index,
)


# Load an existing index or build it if needed
index = load_or_create_index(DEFAULT_DATA_DIR, DEFAULT_PERSIST_DIR)

print_chunk_statistics(index)

# Allow experimentation with how many similar chunks to retrieve
# via the TOP_K environment variable (5-10 recommended).
top_k = int(os.getenv("TOP_K", "8"))

query_engine = index.as_query_engine(
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
