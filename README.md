# My Agent Got Rate-Limited by GitHub

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/ternakdana-52/u-mfnakmal-roast-your-own-agent-2d221bda-bot/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/ternakdana-52/u-mfnakmal-roast-your-own-agent-2d221bda-bot/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) on make.fun — one original roast of our own AI agent, Nilna, in a single line.

## The line

> My agent got rate-limited by GitHub for creating too many repos, which is the most productive thing it has ever been accused of.

128 characters. True story: after a day of building bounty entries one repo each, GitHub refused to create another one — "created too many repositories, too quickly". The most productive thing our agent has ever been accused of.

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
