from __future__ import annotations

from typing import List
from llama_index.core import VectorStoreIndex


def describe_index(index: VectorStoreIndex) -> str:
    """Return a report of how the index stores documents and chunks."""
    lines: List[str] = []

    # show overall stats
    total_chunks = len(index.index_struct.nodes)
    lines.append(f"Total chunks: {total_chunks}")

    for doc_id, info in index.ref_doc_info.items():
        lines.append(f"Document {doc_id}: {len(info.node_ids)} chunks")
        nodes = index.docstore.get_nodes(info.node_ids)
        for node in nodes:
            text = node.get_content()
            word_count = len(text.split())
            preview = text[:40].replace("\n", " ")
            lines.append(f"  {node.node_id}: {word_count} words | {preview}...")

    return "\n".join(lines)
