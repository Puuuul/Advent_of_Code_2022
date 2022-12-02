import toolbox


def method():
    lines = toolbox.open_and_read("input/day1.txt")
    calories = [0]
    for line in lines:
        if line == "\n":
            calories.append(0)
        else:
            calories[len(calories)-1] += int(line)
    print(max(calories))
    mx = 0
    for i in range(3):
        x = calories.pop(calories.index(max(calories)))
        mx += x
    print(mx)


method()
