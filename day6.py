import toolbox
from collections import Counter


def method1():
    line = toolbox.open_and_read("input/day6.txt")[0]
    for i in range(len(line)-3):
        yes = True
        count = Counter(line[i:i+4])
        for j in range(4):
            if count[line[i+j]] != 1:
                yes = False
        if yes:
            print(count)
            print(i+4)
            break


def method2():
    line = toolbox.open_and_read("input/day6.txt")[0]
    for i in range(len(line)-13):
        yes = True
        count = Counter(line[i:i+14])
        for j in range(14):
            if count[line[i+j]] != 1:
                yes = False
        if yes:
            print(count)
            print(i+14)
            break


method1()
method2()
