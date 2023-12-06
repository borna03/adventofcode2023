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
        if start <= val < (start + range_):
            return val - start + dest
        else:
            return -1

    def define_interval(dest, start, range_):
        return range_ - start + dest

    rows = [item for item in rows[2:] if item != ""]
    index = [i for i, item in enumerate(rows) if 'map' in item] + [len(rows)]

    selected_elements = [rows[start:end] for start, end in zip(index, index[1:])]
    seeds2 = [(seeds[seed], seeds[seed + 1] + seeds[seed]) for seed in range(0, len(seeds), 2)]

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

    # PT 2 +++++++++++++++++++++
    for item in selected_elements:
        nums = item[1:]
        overlap = []

        while len(seeds2) != 0:
            starting_int, ending_int = seeds2[-1]
            seeds2 = seeds2[:-1]
            for num in nums:
                num = num.split()
                dest_ = int(num[0])
                start_ = int(num[1])
                range_ = int(num[2])

                overlap_start = max(starting_int, start_)
                overlap_end = min(ending_int, start_ + range_)

                if overlap_start < overlap_end:
                    overlap.append((define_interval(dest_, start_, overlap_start), define_interval(dest_, start_, overlap_end)))
                    if ending_int > overlap_end:
                        seeds2.append((overlap_end, ending_int))
                    if overlap_start > starting_int:
                        seeds2.append((starting_int, overlap_start))
                    break
            else:
                overlap.append((starting_int, ending_int))
        seeds2 = overlap
    q2 = min(seeds2)
    print(q2[0])


if __name__ == '__main__':
    main()
