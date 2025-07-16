"""Utility script to build and persist the document index."""

import argparse

from .analytics import print_chunk_statistics
from .index_utils import build_index, DEFAULT_DATA_DIR, DEFAULT_PERSIST_DIR


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create and persist the index")
    parser.add_argument(
        "--data-dir",
        default=DEFAULT_DATA_DIR,
        help="Directory containing source documents",
    )
    parser.add_argument(
        "--persist-dir",
        default=DEFAULT_PERSIST_DIR,
        help="Where to store the index",
    )
    args = parser.parse_args()

    index = build_index(args.data_dir, args.persist_dir)
    print("Index built and saved to", args.persist_dir)
    print_chunk_statistics(index)
