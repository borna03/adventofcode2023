from collections import defaultdict


def parse_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def parse_row(row):
    if row == "":
        return None

    key, value = [part.strip() for part in row.split("=")]
    values_inside_parentheses = value[1:-1].split(', ')
    return key, (values_inside_parentheses[0], values_inside_parentheses[1])


def main():
    rows = parse_input()
    instructions = rows[0]

    graph = defaultdict(tuple)
    for row in map(parse_row, rows[1:]):
        if row:
            graph[row[0]] = row[1]

    start = "AAA"
    counter = 0
    steps = 0

    while start != "ZZZ":
        move = graph[start][1] if instructions[counter] == "R" else graph[start][0]
        start = move
        counter = (counter + 1) % len(instructions)
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
