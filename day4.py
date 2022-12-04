import toolbox


def method1():
    lines = toolbox.open_and_read("input/day4.txt")
    count = 0
    for line in lines:
        line = line.strip().split(",")
        for i in range(2):
            line[i] = line[i].split("-")
        for i in range(2):
            if int(line[i][0]) <= int(line[1-i][0]) <= int(line[1-i][1]) <= int(line[i][1]):
                count += 1
                break
    print(count)


def method2():
    lines = toolbox.open_and_read("input/day4.txt")
    count = 0
    for line in lines:
        line = line.strip().split(",")
        for i in range(2):
            line[i] = line[i].split("-")
        for i in range(2):
            if int(line[i][0]) <= int(line[1-i][0]) <= int(line[i][1]) or int(line[i][0]) <= int(line[1-i][1]) <= int(line[i][1]):
                count += 1
                break
    print(count)


method1()
method2()
