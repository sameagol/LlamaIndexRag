from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama

# Configure Ollama as the LLM backend
Settings.llm = Ollama(model="llama2")

# Load documents from the data directory
reader = SimpleDirectoryReader('data')
documents = reader.load_data()

# Build the index
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine()

# Example query
response = query_engine.query('What is LlamaIndex?')
print(response)
