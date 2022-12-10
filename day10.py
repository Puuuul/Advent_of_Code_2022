import math

import numpy

import toolbox


def method1():
    lines = toolbox.open_and_read("input/day10.txt")
    sums = numpy.array([1])
    for line in lines:
        line = line.split(" ")
        if line[0] == "addx":
            sums = numpy.append(sums, [sums[-1], sums[-1] + int(line[1])])
        else:
            sums = numpy.append(sums, sums[-1])
    output = sum(sums[19 + 40 * i] * (20 + 40 * i) for i in range(6))
    print(output)
    print(sums)
    return sums


def method2(sums: list):
    screen = numpy.full((6, 40), " ")
    for i, position in enumerate(sums):
        y = math.floor(i/40)
        x = i % 40
        if x in range(position-1, position+2):
            screen[y][x] = "█"
    for row in screen:
        print("".join(row))


method2(method1())
