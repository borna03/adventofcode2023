import re
import time
import string
from collections import defaultdict
from itertools import product


def idenify_seq(blocks):
    pattern = re.compile(r'[?#]+')
    matches = [(match.group(), match.start(), match.end()) for match in pattern.finditer(blocks)]
    return matches


def find_combinations(input_string, length):
    combinations = []
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]

        if '.' not in substring:
            posibble = True
            if i != 0 and i + length != len(input_string):
                if input_string[i - 1] == '#':
                    posibble = False
            if i + length != len(input_string):
                if input_string[length + i] == '#':
                    posibble = False
            if posibble:
                combinations.append((substring, (i, length)))
    return combinations


def match(curr, nums):
    queue = []
    for item in nums:
        combs = find_combinations(curr, item)
        queue.append(combs)

    all_combinations = list(product(*queue))

    possible = []
    for item in all_combinations:
        temp_max = -1
        append = True
        for pair in item:
            if temp_max == -1:
                temp_max = sum(pair[1])
            else:
                if pair[1][0] <= temp_max:
                    append = False
                    break
                else:
                    temp_max = sum(pair[1])
        if append:
            possible.append(item)

    counter = 0
    for item in possible:
        abc = [char for char in curr]
        for pair in item:
            for i in range(pair[1][1]):
                abc[pair[1][0] + i] = str(pair[1][1])
        result_string = ''.join(abc)
        if "#" not in result_string:
            counter += 1

    return counter


def main():
    with open("d12.txt", "r") as f:
        rows = [line.strip() for line in f]
    N = defaultdict(int)

    q1 = 0
    for item in rows:
        item = item.split()

        arr = item[0]
        numbers_as_strings = item[1].split(',')
        numbers = [int(num) for num in numbers_as_strings]

        ans = match(arr, numbers)
        q1 += ans

    print(q1)


if __name__ == "__main__":
    main()
