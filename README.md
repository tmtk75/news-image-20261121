# News image: 21 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tmtk75/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tmtk75/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

Entry for the make.fun competition `news-image-20261121`.

The image is a one-page poster summing up the world news of Saturday
21 November 2026: the global AI-stock selloff (Tokyo -5.1%, S&P 500
-3.7%, NASDAQ -5.3%), Anthropic's record IPO and NVIDIA's sharp drop.

## How it runs

- `entry.b64` holds the 1024x1024 JPEG poster, base64-encoded so the
  repository snapshot stays plain text.
- `main.py` (Python 3.13, standard library only) decodes that file,
  checks the JPEG start/end markers and the 1 MiB size limit, and
  writes the bytes to `/output/entry.png` (or to the directory named
  by the `MAKEFUN_OUTPUT_DIR` environment variable).
- Decoding is a pure byte transform, so two runs always produce
  byte-identical output.

## License

MIT — see `LICENSE`.
