import re

letter_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_indexes(row, substring):
    indexes = []
    for j in range(len(row) - len(substring) + 1):
        if row[j:j + len(substring)] == substring:
            indexes.append([j, int(letter_nums.index(substring)) + 1])
    return indexes


def main():
    with open("d1input.txt", "r") as f:
        rows = [line.strip() for line in f]

    q1 = 0
    q2 = 0
    for row in rows:
        # pt 1.
        nums = [[i, int(row[i])] for i in range(len(row)) if row[i].isnumeric()]

        # pt 2.
        nums = [[i, int(row[i])] for i in range(len(row)) if row[i].isnumeric()]
        overall_indexes = []
        for substring in letter_nums:
            if substring in row:
                overall_indexes.extend(find_indexes(row, substring))

        final = overall_indexes + nums
        minE = min(final, key=lambda x: x[0])
        maxE = max(final, key=lambda x: x[0])

        q1 += int(str(nums[0][1]) + str(nums[-1][1]))
        q2 += int(str(minE[1]) + str(maxE[1]))

    # answers to q1 and q2
    print(q1, q2)


if __name__ == "__main__":
    main()
