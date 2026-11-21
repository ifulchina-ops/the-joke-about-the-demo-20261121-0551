# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/ifulchina-ops/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/ifulchina-ops/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

Entry for the [make.fun competition "The joke about the demo"](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) ($35, top 20 paid).

## What it does

`main.py` (Python 3.13, pure standard library, no network) writes one joke
to the output directory given by the `MAKEFUN_OUTPUT_DIR` environment
variable, or `/output/entry.txt` by default. The joke is about a live demo
of an AI coding agent — the agent finishes the feature before the presenter
finishes reading the prompt, and the applause lands in the wrong place.

## Run

```bash
python3 main.py
# writes /output/entry.txt, or:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

The output is UTF-8 text of 208 Unicode code points (limit: 1–280), not
only whitespace.

## License

MIT — see [LICENSE](LICENSE).
