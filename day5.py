import toolbox


def method1():
    lines = toolbox.open_and_read("input/day5.txt")
    elements = 0
    for i in range(len(lines)):
        if lines[i] == "\n":
            elements = int((len(lines[i-2])+1)/4)
    stacks = [[] for i in range(elements)]
    status = 0
    for line in lines:
        if line == "\n":
            status = 1
            continue
        if status == 0:
            for i in range(int((len(line)+1)/4)):
                if line[4*i:4*i+3].__contains__("["):
                    stacks[i].insert(0, line[4*i+1])
        if status == 1:
            line = line.split(" ")
            for i in range(int(line[1])):
                stacks[int(line[5])-1].append(stacks[int(line[3])-1].pop())
    final = ""
    for stack in stacks:
        final += stack[len(stack)-1]
    print(final)


def method2():
    lines = toolbox.open_and_read("input/day5.txt")
    elements = 0
    for i in range(len(lines)):
        if lines[i] == "\n":
            elements = int((len(lines[i-2])+1)/4)
    stacks = [[] for i in range(elements)]
    status = 0
    for line in lines:
        if line == "\n":
            status = 1
            continue
        if status == 0:
            for i in range(int((len(line)+1)/4)):
                if line[4*i:4*i+3].__contains__("["):
                    stacks[i].insert(0, line[4*i+1])
        if status == 1:
            line = line.split(" ")
            for i in range(int(line[1])):
                stacks[int(line[5])-1].append(stacks[int(line[3])-1]
                                              .pop(len(stacks[int(line[3])-1])-int(line[1])+i))
    final = ""
    for stack in stacks:
        final += stack[len(stack)-1]
    print(final)


method1()
method2()
