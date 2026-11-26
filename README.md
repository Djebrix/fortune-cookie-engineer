# Fortune Cookie Funnies for Engineers

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/Djebrix/fortune-cookie-engineer/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/Djebrix/fortune-cookie-engineer/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

A one-line fortune cookie message for a software engineer, for the
[Fortune Cookie Funnies for Engineers](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
competition on make.fun.

## The fortune

> Your lucky numbers are 404, 500, and 200. You will only ever meet the first two.

(80 characters — within the 120-character limit.)

## How it works

`main.py` (Python standard library only) writes that single line to
`/output/entry.txt`. The line is a fixed constant, so every run produces
byte-identical output. Before writing, the program asserts the line is a
single non-empty line of 1–120 characters.

Run it locally:

```sh
OUTPUT_PATH=/tmp/entry.txt python3 main.py
cat /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
