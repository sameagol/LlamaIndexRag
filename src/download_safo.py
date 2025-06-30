import re
import time
from pathlib import Path
import argparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE = "https://www.faa.gov"
LIST_URL = f"{BASE}/other_visit/aviation_industry/airline_operators/airline_safety/safo/all_safos"


def download_safo(output_dir: str) -> None:
    """Download all SAFO PDFs to the given directory."""
    out = Path(output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    response = requests.get(LIST_URL, timeout=30)
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = {
        BASE + a["href"]
        for a in soup.find_all("a", href=re.compile(r"\.pdf$", re.I))
    }

    for url in tqdm(sorted(pdf_links), desc="Downloading SAFOs"):
        fname = out / url.split("/")[-1]
        if fname.exists():
            continue
        r = requests.get(url, timeout=60)
        fname.write_bytes(r.content)
        time.sleep(0.2)

    print(f"Saved {len(list(out.glob('*.pdf')))} SAFO PDFs \u2192 {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download Safety Alerts for Operators (SAFO) PDFs"
    )
    parser.add_argument(
        "--output-dir",
        default="data/safo",
        help="Destination directory",
    )
    args = parser.parse_args()
    download_safo(args.output_dir)
