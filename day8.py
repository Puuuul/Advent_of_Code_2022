import toolbox
import numpy as np


def look_around(arr, i, j):
    directions = [[1, 0], [-1, 0]]
    val = arr[i][j]
    score = [0, 1]
    for a in range(2):
        for b in range(2):
            dirx = directions[a][b]
            diry = directions[a][1 - b]
            distance = 1
            if 0 <= i + dirx <= len(arr)-1 and 0 <= j + diry <= len(arr[0])-1:
                x = i + dirx
                y = j + diry
            else:
                score[0] = 1
                continue
            while True:
                if arr[x][y] >= val:
                    score[1] = score[1]*distance
                    break
                elif not (0 < x < len(arr)-1 and 0 < y < len(arr[0])-1):
                    score[0] = 1
                    score[1] = score[1] * distance
                    break
                else:
                    x += dirx
                    y += diry
                    distance += 1
    return score


def method():
    lines = np.array([[int(c) for c in line.strip()] for line in toolbox.open_and_read("input/day8.txt")])
    visible = 0
    score = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            new = look_around(lines, i, j)
            visible += new[0]
            if new[1] > score:
                score = new[1]
    print(visible)
    print(score)


method()
