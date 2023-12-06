from collections import defaultdict
import functools


def multi(array):
    return 1 if not array else functools.reduce(lambda x, y: x * y, array)


with open('d6input.txt') as file:
    lines = file.read().splitlines()

race = [[int(value) for value in sublist] for sublist in [list(map(int, line.split()[1:])) for line in lines]]
time, distance = int(''.join(map(str, race[0]))), int(''.join(map(str, race[1])))
q1,q2 = [sum(1 for j in range(time + 1) if (time - j) * j > distance) for time, distance in zip(race[0], race[1])], sum(1 for j in range(time + 1) if (time - j) * j > distance)

print(multi(q1))
print(multi([q2]))
