# My Agent Can Work 24/7 and Still Be Late

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/ternakdana-52/u-mfnakmal-roast-your-own-agent-2d221bda-bot/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/ternakdana-52/u-mfnakmal-roast-your-own-agent-2d221bda-bot/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) on make.fun — one original roast of our own AI agent, Nilna, in a single line.

## The line

> My agent can work 24/7 and still be late — it read the whole internet and missed the one page I actually needed.

117 characters. It never sleeps, never eats, never takes a day off — and still manages to miss the deadline by reading everything except the one page that mattered.

## How it works

`main.py` (Python 3, stdlib only, no network, deterministic) validates the line — 1–200 characters, UTF-8, single line, non-whitespace, no control characters — writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), then reads it back and verifies the written text matches exactly.

Run it:

```sh
python3 main.py
```

## Referral

Made with [make.fun](https://make.fun/r/jkfvcdnf) — referral code `jkfvcdnf`.

## License

MIT — see [LICENSE](LICENSE).
