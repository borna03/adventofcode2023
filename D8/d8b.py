import sys
from collections import defaultdict
from math import gcd


def parse_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def parse_row(row):
    if row == "":
        return None

    key, value = map(str.strip, row.split("="))
    values_inside_parentheses = value[1:-1].split(', ')
    return key, (values_inside_parentheses[0], values_inside_parentheses[1])


def find_starting_nodes(graph):
    return [key for key in graph.keys() if key.endswith("A")]


def calculate_steps(start, instructions, graph):
    counter = 0
    steps = 0
    while not start.endswith("Z"):
        move = graph[start][1] if instructions[counter] == "R" else graph[start][0]
        start = move
        counter = (counter + 1) % len(instructions)
        steps += 1
    return steps


def main():
    rows = parse_input()
    instructions = rows[0]
    graph = defaultdict(tuple)

    for row in map(parse_row, rows[1:]):
        if row:
            graph[row[0]] = row[1]

    start_nodes = find_starting_nodes(graph)
    q2 = [calculate_steps(start, instructions, graph) for start in start_nodes]

    lcm = 1
    for steps in q2:
        lcm = lcm * steps // gcd(lcm, steps)

    print(lcm)


if __name__ == "__main__":
    main()
