import re
from functools import partial
import time
import string

blue = 14
red = 12
green = 13


def main():
    start_time = time.time()

    colors = {"blue": 14, "green": 13, "red": 12}

    with open("d2input.txt", "r") as f:
        rows = [line.strip() for line in f]

    q1 = 0
    q2 = []
    for row in rows:
        #pt 1
        row = row.split(':')
        game_id = re.split('[;,]', row[0])
        game_id = re.findall(r'\d+', game_id[0])

        row = re.split(r'[,;]', row[1])
        counter = True

        #pt 2
        min_colors = {"blue": 1, "green": 1, "red": 1}

        for ball in row:
            ball = ball.strip()
            number, color = ball.split(" ", 1)
            if int(number) > min_colors[color]:
                min_colors[color] = int(number)

            if int(number) > int(colors[color]):
                counter = False

        if counter:
            q1 += int(game_id[0])

        product = 1
        for color, value in min_colors.items():
            product *= value

        q2.append(product)

    # answers to q1 and q2
    print(q1, sum(q2))

    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    main()
