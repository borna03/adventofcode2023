from collections import defaultdict
import functools
import re
import time
from collections import Counter
import string
from itertools import product

with open("input.txt") as file:
    lines = file.read().splitlines()


def determine(item: tuple[str, int]) -> tuple[int, list[int]]:
    hand, bid = item

    counts = sorted(list(Counter(hand.replace("J", "")).values()))
    if len(counts) > 0:
        counts[-1] += hand.count("J")
    else:
        counts.append(5)
    if 5 in counts:
        type = 8
    elif 4 in counts:
        type = 7
    elif 3 in counts:
        type = 6 if 2 in counts else 5
    elif 2 in counts:
        type = 4 if counts.count(2) == 2 else 3
    else:
        type = 2

    vals = "J23456789TQKA"
    sec_val = []
    for char in hand:
        for i in range(len(vals)):
            if char == vals[i]:
                sec_val.append(i)
    return (type, sec_val)


hands = []
for row in lines:
    row = row.split()
    hands.append((row[0], row[1]))

hands = sorted(hands, key=determine)
q1 = sum((int(bid) * (i + 1) for i, (hand, bid) in enumerate(hands)))
print(q1)
