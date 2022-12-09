import math
import toolbox
from collections import defaultdict


def method(length):
    lines = toolbox.open_and_read("input/day9.txt")
    rope = [[0, 0] for i in range(length)]
    visited = defaultdict(int)
    visited[str([0, 0])] = 1
    switch = {"U": (1, 1), "D": (1, -1), "L": (0, -1), "R": (0, 1)}
    for line in lines:
        line = line.split(" ")
        for x in range(int(line[1])):
            direction = switch[line[0]]
            rope[0][direction[0]] += direction[1]
            for i in range(length-1):
                if math.sqrt(pow(rope[i + 1][0] - rope[i][0], 2) + pow(rope[i + 1][1] - rope[i][1], 2)) > math.sqrt(2):
                    for a in range(2):
                        if rope[i][a] - rope[i+1][a] == 0:
                            continue
                        rope[i+1][a] += math.copysign(1, rope[i][a] - rope[i+1][a])
            visited[str(rope[len(rope)-1])] += 1
    print(len(visited))


method(2)
method(10)
