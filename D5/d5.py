import re
import time
import string
from collections import defaultdict
import math


def main():
    with open("d5input.txt", "r") as f:
        rows = [line.strip() for line in f]

    seeds = rows[0]
    seeds = seeds.split(":")
    seeds = [int(seed) for seed in seeds[1].split()]

    def find(dest, start, range_, val):
        if val:
            return range_ - start + dest
        else:
            if start <= val < (start + range_):
                return val - start + dest
            else:
                return -1

    rows = [item for item in rows[2:] if item != ""]
    index = [i for i, item in enumerate(rows) if 'map' in item] + [len(rows)]

    selected_elements = [rows[start:end] for start, end in zip(index, index[1:])]

    # PT 1 +++++++++++++++++++++
    q1 = []
    for seed in seeds:
        start = seed
        for item in selected_elements:
            nums = item[1:]
            for num in nums:
                num = num.split()
                dest_ = int(num[0])
                start_ = int(num[1])
                range_ = int(num[2])

                val = find(dest_, start_, range_, start)
                if val != -1:
                    break

            if val != -1:
                start = val

        q1.append(start)
    print(min(q1))

    # for row in rows:
    #     print(row)

    seeds2 = [(seeds[seed], seeds[seed + 1] + seeds[seed]) for seed in range(0, len(seeds), 2)]
    # PT 2 +++++++++++++++++++++
    for item in selected_elements:
        nums = item[1:]
        overlap = []

        while len(seeds2) > 0:
            s, e = seeds2.pop()
            for num in nums:
                num = num.split()
                dest_ = int(num[0])
                start_ = int(num[1])
                range_ = int(num[2])

                overlap_start = max(s, start_)
                overlap_end = min(e, start_ + range_)

                if overlap_start < overlap_end:
                    overlap.append((find(dest_, start_, overlap_start, True), find(dest_, start_, overlap_end, True)))
                    if overlap_start > s:
                        seeds2.append((s, overlap_start))
                    if e > overlap_end:
                        seeds2.append((overlap_end, e))
                    break
            else:
                overlap.append((s, e))
        seeds2 = overlap
    print(min(seeds2)[0])


if __name__ == "__main__":
    main()
