from collections import defaultdict
import functools
import re
import time
from collections import Counter
import string
from itertools import product


def parse_input(filename="d9input.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def is_all_zeros(arr):
    return all(element == 0 for element in arr)


def process_rows(row, ans1=0, temp=None):
    if temp is None:
        temp = []
    temp.append(row)

    ans1 += int(row[-1])
    if is_all_zeros(row):
        return ans1, temp
    else:
        next_row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        return process_rows(next_row, ans1, temp)


def main():
    rows = parse_input()
    N = defaultdict(int)
    q1 = 0
    q2 = 0
    for row in rows:
        row = [int(row) for row in row.split(" ")]
        # q1
        ans1, temp = process_rows(row)
        q1 += ans1

        # q2
        ans2 = []
        for i in range(len(temp) - 1 - 1, -1, -1):
            ans2.append(temp[i][0] - temp[i + 1][0])
            temp[i].insert(0, temp[i][0] - temp[i + 1][0])

        q2 += ans2[-1]
    print(q1, q2)


if __name__ == "__main__":
    main()
