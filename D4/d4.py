import re
import time
import string


def main():
    start_time = time.time()

    with open("d4input.txt", "r") as f:
        rows = [line.strip() for line in f]

    num_pattern = r'\d+'
    q1 = 0
    q2 = {key: 1 for key in range(0, len(rows))}
    for i, line in enumerate(rows):
        row = rows[i].split(':')
        nums, my_nums = re.findall(num_pattern, row[1].split("|")[0]), re.findall(num_pattern, row[1].split("|")[1])
        nums, my_nums = list(map(int, nums)), list(map(int, my_nums))

        # pt1
        points = 2 ** (len(set(nums).intersection(set(my_nums))) - 1)  # -1 because it has to start from exponent 0 (1,2,4,8,...)
        if isinstance(points, int):
            q1 += points

        # pt2
        for j in range(len(set(nums).intersection(set(my_nums)))):
            q2[i + j + 1] += q2[i]

    print(q1, sum(q2.values()))

    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    main()
