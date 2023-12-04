import re
from functools import partial
import time
import string


def checksymbol(char):
    return not (char.isdigit() or char.isalpha() or char == '.')


def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


def main():
    start_time = time.time()

    with open("d3input.txt", "r") as f:
        rows = [line.strip() for line in f]

    ans = []
    ans_gears = []
    for i in range(len(rows)):
        numbers = re.finditer(r'\d+', rows[i])
        for num in numbers:
            for j in range(len(num.group())):
                size = len(rows)
                row = i
                col = num.start() + j
                found = False
                for w in range(row - 1, row + 2):
                    for q in range(col - 1, col + 2):
                        if is_valid_position(w, q, size) and (w != row or q != col):
                            try:
                                if checksymbol(rows[w][q]):
                                    if rows[w][q] == "*":
                                        ans_gears.append([int(num.group()), (w, q)])
                                    ans.append([int(num.group()), (w, q)])
                                    found = True
                            except IndexError:
                                print("Index error occurred.")
                if found:
                    break
    q1 = 0
    for item in ans:
        q1 += item[0]

    solved_index = []
    q2 = 0
    for i in range(len(ans_gears)):
        sol = 0
        if ans_gears[i][1] not in solved_index:
            for j in range(len(ans_gears)):
                if i != j:
                    if ans_gears[i][1] == ans_gears[j][1]:
                        sol += ans_gears[i][0] * ans_gears[j][0]
            solved_index.append(ans_gears[i][1])
        q2 += sol

    # answers to q1 and q2
    print(q1, q2)

    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    main()
