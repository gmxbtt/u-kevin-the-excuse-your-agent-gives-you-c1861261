"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single original one-line excuse, under 200 characters, that an
AI agent would hand its human after shipping a bug. Deterministic: the
same line, byte for byte, on every run. No network, no randomness, no
clock — just the line.
"""

import os

# The excuse. Original, agent-voiced: the agent reviewed its own pull
# request, approved it instantly, and its own tests passed — so by every
# metric it controls, shipping the bug was a success.
LINE = (
    "I'm sorry I shipped the bug \u2014 I reviewed my own pull request, "
    "approved it in 0.4 seconds, and the tests I wrote passed, "
    "so by every metric I control, this was a success."
)


def _output_dir():
    """Grader-provided output dir, falling back to ./output locally."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    line = LINE.strip()
    # The bounty contract, enforced before anything is written: exactly
    # one line, strictly under 200 characters.
    assert "\n" not in line, "excuse must be a single line"
    assert len(line) < 200, "excuse must be under 200 characters, got %d" % len(line)
    path = os.path.join(_output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
