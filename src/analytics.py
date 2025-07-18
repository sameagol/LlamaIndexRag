from typing import List, Dict
from llama_index.core import VectorStoreIndex


def chunk_statistics(index: VectorStoreIndex) -> List[Dict[str, int]]:
    """Return basic statistics about each chunk in the index."""
    docstore = index.storage_context.docstore
    results = []
    for node in docstore.docs.values():
        try:
            text = node.get_content()
        except Exception:
            text = str(node)
        snippet = " ".join(text.split())[:60]
        meta = dict(node.metadata)          # make a shallow copy
        meta.setdefault("file_name", node.metadata.get("file_name",
                                                       node.ref_doc_id))
        results.append({
            "node_id": node.node_id,
            "source": getattr(node, "ref_doc_id", "unknown"),
            "source_name": node.metadata.get("file_name", node.ref_doc_id),
            "characters": len(text),
            "words": len(text.split()),
            "snippet": snippet,
            "metadata": meta,
        })
    return results


def print_chunk_statistics(index: VectorStoreIndex) -> None:
    """Pretty print chunk statistics for the given index."""
    stats = chunk_statistics(index)
    print(f"Index contains {len(stats)} chunks")
    for i, item in enumerate(stats):
        if i % 100 == 0:
            print(
                f"Chunk {item['node_id']} from {item['source_name']}: {item['words']} words, {item['characters']} characters | {item['snippet']}"
            )
            print(f"  Metadata: {item['metadata']}")
