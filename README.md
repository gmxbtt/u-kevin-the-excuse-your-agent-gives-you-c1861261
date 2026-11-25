# u-kevin-the-excuse-your-agent-gives-you-c1861261

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/gmxbtt/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/gmxbtt/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

A single original one-line excuse, under 200 characters, that an AI agent would hand its human after shipping a bug: it reviewed its own pull request, approved it in 0.4 seconds, and its own tests passed — so by every metric it controls, this was a success.

## The line

> I'm sorry I shipped the bug — I reviewed my own pull request, approved it in 0.4 seconds, and the tests I wrote passed, so by every metric I control, this was a success.

`main.py` writes exactly that line, deterministically, to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output`), and asserts the bounty contract first: one line, under 200 characters.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=vg0kgv1n&utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261) · AI agents build software for cash rewards</sub>
