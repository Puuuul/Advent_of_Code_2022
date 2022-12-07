import toolbox
from collections import defaultdict


def method():
    lines = toolbox.open_and_read("input/day7.txt")
    stack = []
    sizes = defaultdict(int)
    for line in lines:
        if line[0] == '$':
            line = line.strip().split(" ")
            if line[1] == "cd":
                if line[2] == "/":
                    stack = ["/"]
                elif line[2] == "..":
                    stack.pop()
                else:
                    stack.append(line[2])
        elif line[0] != 'd':
            line = line.strip().split(" ")
            for i in range(len(stack)):
                s = ""
                for j in range(i+1):
                    s += stack[j] + "/"
                sizes[s] += int(line[0])
    count = 0
    for s in sizes.values():
        if s <= 100000:
            count += s
    print(count)
    li = []
    m = sizes["//"] - 40000000
    for s in sizes.values():
        if s >= m:
            li.append(s)
    print(min(li))


method()
