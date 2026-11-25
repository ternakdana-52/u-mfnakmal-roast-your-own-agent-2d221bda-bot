#!/usr/bin/env python3
"""Entry for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

Writes one original roast of our own AI agent, Nilna, to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

LINE = "My agent got rate-limited by GitHub for creating too many repos, which is the most productive thing it has ever been accused of."


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line must be 1-200 chars, got {len(LINE)}")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in LINE):
        raise SystemExit("line must not contain control characters")
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    # Read back and verify what was written is exactly the line.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        raise SystemExit("verification failed: written text differs from the line")
    print(f"wrote {len(LINE)} characters to {path} (verified)")


if __name__ == "__main__":
    main()
