import toolbox


def method1():
    lines = toolbox.open_and_read("input/day3.txt")
    val = 0
    for line in lines:
        c1 = line[0:len(line) // 2]
        c2 = line[len(line) // 2:]
        for c in c1:
            if c2.__contains__(c):
                if c.islower():
                    val += ord(c) - 96
                else:
                    val += ord(c) - 38
                break
    print(val)


def method2():
    lines = toolbox.open_and_read("input/day3.txt")
    val = 0
    for i in range(int(len(lines)/3)):
        for c in lines[i*3]:
            if lines[i*3+1].__contains__(c) and lines[i*3+2].__contains__(c):
                if c.islower():
                    val += ord(c) - 96
                else:
                    val += ord(c) - 38
                break
    print(val)


method1()
method2()
