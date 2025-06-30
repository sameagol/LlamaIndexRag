import os
import urllib.request
import argparse

AIM_URL = "https://www.faa.gov/air_traffic/publications/atpubs/aim_basic/aim.pdf"


def download_aim(output_path: str) -> None:
    """Download the AIM Basic PDF to the given path."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"Downloading {AIM_URL} to {output_path}...")
    urllib.request.urlretrieve(AIM_URL, output_path)
    print("Download complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download the Aeronautical Information Manual (AIM) Basic PDF"
    )
    parser.add_argument(
        "--output",
        default="data/aim_basic.pdf",
        help="Destination file path",
    )
    args = parser.parse_args()
    download_aim(args.output)
