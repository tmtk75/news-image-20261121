"""Entry program for make.fun news-image-20261121.

The poster image for Saturday 21 November 2026 (the global AI-stock
selloff) ships inside this repository as a base64 text file, because the
repo snapshot is handled as plain text.  This program restores the
original JPEG bytes and stores them under the required output name.
Decoding base64 is deterministic, so repeated runs emit the same file.
"""

import base64
import os
import sys
from pathlib import Path

IMAGE_PAYLOAD_NAME = "entry.b64"
OUTPUT_NAME = "entry.png"
JPEG_SOI = b"\xff\xd8"
JPEG_EOI = b"\xff\xd9"
MAX_IMAGE_BYTES = 1_048_576


def load_image_bytes(repo_dir: Path) -> bytes:
    payload_path = repo_dir / IMAGE_PAYLOAD_NAME
    if not payload_path.is_file():
        raise FileNotFoundError(f"image payload not found: {payload_path}")
    encoded = payload_path.read_bytes()
    cleaned = b"".join(encoded.split())
    if not cleaned:
        raise ValueError("image payload file is empty")
    return base64.b64decode(cleaned, validate=True)


def resolve_output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(chosen)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def check_image_bytes(payload: bytes) -> None:
    # The gate reads the output by its first bytes, so make sure the
    # decoded payload really is a complete JPEG before writing it out.
    if not payload.startswith(JPEG_SOI):
        raise ValueError("decoded payload does not start with a JPEG SOI marker")
    if not payload.endswith(JPEG_EOI):
        raise ValueError("decoded payload does not end with a JPEG EOI marker")
    if len(payload) > MAX_IMAGE_BYTES:
        raise ValueError("decoded payload exceeds the 1 MiB competition limit")


def main() -> int:
    here = Path(__file__).resolve().parent
    payload = load_image_bytes(here)
    check_image_bytes(payload)
    target = resolve_output_dir() / OUTPUT_NAME
    target.write_bytes(payload)
    print(f"wrote {target} ({len(payload)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
