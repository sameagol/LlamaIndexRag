from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


DEFAULT_DATA_DIR = "data"
DEFAULT_PERSIST_DIR = "index_storage"


# Configure global defaults so imported scripts don't need to
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(
    model="llama3.1",
    request_timeout=360.0,
    context_window=8000,
)


def build_index(data_dir: str = DEFAULT_DATA_DIR, persist_dir: str = DEFAULT_PERSIST_DIR) -> VectorStoreIndex:
    """Create a new index from documents in ``data_dir`` and persist it."""
    documents = SimpleDirectoryReader(data_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir)
    return index


def load_index(persist_dir: str = DEFAULT_PERSIST_DIR) -> VectorStoreIndex:
    """Load an existing index from ``persist_dir``."""
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    return load_index_from_storage(storage_context)


def load_or_create_index(data_dir: str = DEFAULT_DATA_DIR, persist_dir: str = DEFAULT_PERSIST_DIR) -> VectorStoreIndex:
    """Load an index if it exists, otherwise create a new one."""
    if Path(persist_dir).exists():
        return load_index(persist_dir)
    return build_index(data_dir, persist_dir)
