#!/usr/bin/env python3
"""Best Advice I Ever Got — entry program.

Writes one sentence, the best advice the writer ever received, to
/output/entry.txt. The line is 103 characters, a single sentence.
"""

import os

LINE = (
    "My grandfather said the money comes back and the time does not, "
    "and he said it the week before he died."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
