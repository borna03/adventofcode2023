from collections import defaultdict
import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
from itertools import combinations
from collections import deque


def insert_column(matrix, column_index, character):
    for i in range(len(matrix)):
        row_as_list = list(matrix[i])
        row_as_list.insert(column_index, character)
        matrix[i] = ''.join(row_as_list)


# def add_row(matrix, row):
# matrix[row].append(['.' for i in range(len(matrix[0]))])


def generate_all_combinations(array):
    all_combinations = list(combinations(array, 2))
    return all_combinations


def main():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    emptyr = [i for i in range(len(lines))]
    emptyc = [j for j in range(len(lines[0]))]
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] == '#':
                if i in emptyr:
                    emptyr.remove(i)
                if j in emptyc:
                    emptyc.remove(j)

    # counter = 0
    # for item in emptyc:
    #     insert_column(lines, item + counter, '.')
    #     counter += 1
    #
    # counter2 = 0
    #
    # empty = ''
    # for i in range(len(lines[0])):
    #     empty += '.'
    # for item in emptyr:
    #     lines.insert(item + counter2, empty)
    #     counter2 += 1

    points = []
    c = 1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                points.append((i, j, c))
                c += 1
    q1 = []
    q2 = []
    result = generate_all_combinations(points)
    for item in result:
        a, b = item[0], item[1]
        ccounterq1 = 0
        rcounterq1 = 0

        ccounterq2 = 0
        rcounterq2 = 0

        for skip in emptyc:
            if a[1] < skip < b[1] or a[1] > skip > b[1]:
                ccounterq2 += 10**6 - 1
                ccounterq1 += 1
        for skip in emptyr:
            if a[0] < skip < b[0] or a[0] > skip > b[0]:
                rcounterq1 += 1
                rcounterq2 += 10**6 -1

        distance1 = abs(a[0] - b[0]) + abs(a[1] - b[1]) + rcounterq1 + ccounterq1
        distance2 = abs(a[0] - b[0]) + abs(a[1] - b[1]) + rcounterq2 + ccounterq2

        q1.append(distance1)
        q2.append(distance2)
    print(sum(q1),sum(q2))


if __name__ == "__main__":
    main()
