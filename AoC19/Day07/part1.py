import sys
from copy import deepcopy

def main(opcodes, first_code, second_code):
    index = 0
    first_opcode = opcodes[index]
    done_first = False

    while first_opcode != 99:
        action = first_opcode % 10

        first = (first_opcode % 1000) // 100
        second = (first_opcode % 10000) // 1000
        third = (first_opcode % 100000) // 10000

        if action == 1:
            val_one = opcodes[opcodes[index + 1]] if not first else opcodes[index + 1]
            val_two = opcodes[opcodes[index + 2]] if not second else opcodes[index + 2]
            opcodes[opcodes[index + 3]] = val_one + val_two
            index += 4
        elif action == 2:
            val_one = opcodes[opcodes[index + 1]] if not first else opcodes[index + 1]
            val_two = opcodes[opcodes[index + 2]] if not second else opcodes[index + 2]
            opcodes[opcodes[index + 3]] = val_one * val_two
            index += 4
        elif action == 3:
            if done_first:
                value = second_code
            else:
                value = first_code
                done_first = True
            opcodes[opcodes[index + 1]] = value
            index += 2
        elif action == 4:
            return opcodes[opcodes[index + 1]]
            index += 2
        elif action == 5:
            val_one = opcodes[opcodes[index + 1]] if not first else opcodes[index + 1]
            val_two = opcodes[opcodes[index + 2]] if not second else opcodes[index + 2]
            if val_one:
                index = val_two
            else:
                index += 3
        elif action == 6:
            val_one = opcodes[opcodes[index + 1]] if not first else opcodes[index + 1]
            val_two = opcodes[opcodes[index + 2]] if not second else opcodes[index + 2]
            if not val_one:
                index = val_two
            else:
                index += 3
        elif action == 7:
            val_one = opcodes[opcodes[index + 1]] if not first else opcodes[index + 1]
            val_two = opcodes[opcodes[index + 2]] if not second else opcodes[index + 2]
            if val_one < val_two:
                opcodes[opcodes[index + 3]] = 1
            else:
                opcodes[opcodes[index + 3]] = 0
            index += 4
        elif action == 8:
            val_one = opcodes[opcodes[index + 1]] if not first else opcodes[index + 1]
            val_two = opcodes[opcodes[index + 2]] if not second else opcodes[index + 2]
            if val_one == val_two:
                opcodes[opcodes[index + 3]] = 1
            else:
                opcodes[opcodes[index + 3]] = 0
            index += 4

        first_opcode = opcodes[index]

def max_thruster_signal(opcodes, available, last_result):
    global MAX
    if not available:
        MAX = max(MAX, last_result)

    for index, value in enumerate(available):
        new_available = deepcopy(available)
        new_available.pop(index)
        c = main(deepcopy(opcodes), value, last_result)
        max_thruster_signal(opcodes, new_available, c)

MAX = float("-inf")
opcodes = list(map(int, input().split(',')))
available = [0, 1, 2, 3, 4]

max_thruster_signal(opcodes, available, 0)
print(MAX)
