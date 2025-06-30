from typing import Sequence, List
from llama_index.core.schema import Document
from llama_index.readers.smart_pdf_loader import SmartPDFLoader


def load_pdfs(paths: Sequence[str]) -> List[Document]:
    """Load one or more PDFs using SmartPDFLoader."""
    loader = SmartPDFLoader()
    documents: List[Document] = []
    for path in paths:
        documents.extend(loader.load_data(str(path)))
    return documents
