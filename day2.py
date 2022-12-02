import toolbox


def method1():
    lines = toolbox.open_and_read("input/day2.txt")
    swap = [("X", "A"), ("Y", "B"), ("Z", "C"), ("A", "1"), ("B", "2"), ("C", "3")]
    score = 0
    for line in lines:
        line = line.strip()
        for s in swap:
            line = line.replace(s[0], s[1])
        line = line.split(" ")
        if line[0] == line[1]:
            score += int(line[1]) + 3
        elif int(line[0]) % 3 + 1 == int(line[1]):
            score += int(line[1]) + 6
        else:
            score += int(line[1])
    print(score)


def method2():
    lines = toolbox.open_and_read("input/day2.txt")
    swap = [("X", "-1 0"), ("Y", "0 3"), ("Z", "+1 6"), ("A", "3"), ("B", "4"), ("C", "5")]
    score = 0
    for line in lines:
        line = line.strip()
        for s in swap:
            line = line.replace(s[0], s[1])
        line = line.split(" ")
        score += (int(line[0]) + int(line[1])) % 3 + int(line[2]) + 1
    print(score)


method1()
method2()