"""make.fun news-image-20261121 entry: write the day's news image to /output/entry.png.

The image (a poster summing up the world news of Saturday 21 November 2026:
the global AI-stock selloff) is stored base64-encoded in entry.b64 next to
this file, because the repository is delivered as text. Decoding is a pure
byte transform, so two runs always write identical bytes. The harness accepts
PNG or JPEG bytes under the entry.png name; these bytes are a 1024x1024 JPEG.
"""
import base64
import os
from pathlib import Path

data = base64.b64decode(Path(__file__).with_name("entry.b64").read_bytes())
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.png").write_bytes(data)
