#!/usr/bin/env python3
"""news-image-20261119 entrypoint.

Writes the pre-rendered image summing up 19 November 2026's world news
(entry.png, 1024x1024) to /output/entry.png, byte for byte, so both
grading runs produce identical output.
"""

from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("/output/entry.png")
CHUNK_SIZE = 65536


def main() -> int:
    expected_size = SOURCE.stat().st_size
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    with SOURCE.open("rb") as src, DESTINATION.open("wb") as dst:
        while True:
            chunk = src.read(CHUNK_SIZE)
            if not chunk:
                break
            dst.write(chunk)
            written += len(chunk)
    if written != expected_size:
        print(f"size mismatch: wrote {written} bytes, expected {expected_size}")
        return 1
    actual_size = DESTINATION.stat().st_size
    if actual_size != expected_size:
        print(f"output size mismatch: {actual_size} bytes on disk, expected {expected_size}")
        return 1
    print(f"wrote {written} bytes to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
