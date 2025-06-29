import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Set your OpenAI API key
os.environ.setdefault('OPENAI_API_KEY', 'sk-...')  # TODO: replace with your key

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
