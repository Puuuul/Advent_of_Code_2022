import math

import toolbox


class Monkey:
    def __int__(self, items, operation, test, true_monkey, false_monkey, inspected):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueMonkey = true_monkey
        self.falseMonkey = false_monkey
        self.inspected = inspected


def method(iterations, dividend):
    lines = toolbox.open_and_read("input/day11.txt")
    monkeys = monkey_setup(lines)
    modulo = 1
    for m in monkeys:
        modulo = modulo * m.test
    for x in range(iterations):
        monkeys = monkey_keep_away(monkeys, dividend, modulo)
    monkey_business = sorted([m.inspected for m in monkeys], reverse=True)
    print(monkey_business[0]*monkey_business[1])


def monkey_setup(lines):
    monkeys = []
    for i, line in enumerate(lines):
        line = line.strip().replace(",", "").split(" ")
        current = i % 7
        if current == 0:
            monkeys.append(Monkey())
            monkeys[-1].inspected = 0
        elif current == 1:
            monkeys[-1].items = [int(s) for s in line[2:]]
        elif current == 2:
            monkeys[-1].operation = line[4:]
        elif current == 3:
            monkeys[-1].test = int(line[-1])
        elif current == 4:
            monkeys[-1].trueMonkey = int(line[-1])
        elif current == 5:
            monkeys[-1].falseMonkey = int(line[-1])
    return monkeys


def monkey_keep_away(monkeys, dividend, modulo):
    for i, monkey in enumerate(monkeys):
        while monkeys[i].items:
            worry = monkeys[i].items.pop()
            m, w = monkey_inspect(monkey, worry, dividend, modulo)
            monkeys[m].items.append(w)
            monkeys[i].inspected += 1
    return monkeys


def monkey_inspect(monkey, worry, dividend, modulo):
    num = int(monkey.operation[1].replace("old", str(worry)))
    if monkey.operation[0] == "+":
        worry += num
    else:
        worry = worry * num
    worry = math.floor(worry / dividend)
    if worry % monkey.test == 0:
        return monkey.trueMonkey, worry % modulo
    else:
        return monkey.falseMonkey, worry % modulo


method(20, 3)
method(10000, 1)
