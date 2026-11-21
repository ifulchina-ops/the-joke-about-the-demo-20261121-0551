#!/usr/bin/env python3
"""The joke about the demo — make.fun competition entry.

Writes one short joke to the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (or /output/entry.txt
by default). Pure standard library, no network access.

The joke is about a live demo of an AI coding agent, in front
of a real audience: the agent builds the feature, runs the
tests, and fixes its own bug before the presenter has even
finished reading the prompt out loud. The laugh lands on the
last line — the applause belongs to the code, and the silence
belongs to the human who was supposed to be presenting.
The joke is 208 Unicode code points, inside the 1-280 gate.
"""

import os

JOKE = (
    "Live demo, two hundred people watching: the agent built "
    "the feature, ran the tests, and fixed its own bug before "
    "I finished reading the prompt out loud. "
    "The applause was for the code — the silence was for me."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
