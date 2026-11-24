import os

TEXT = (
    "Today my agent booked me a flight to Paris, Texas, because the "
    "Eiffel Tower there had shorter lines and better reviews."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, f"entry must be 1-200 characters, got {len(TEXT)}"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
