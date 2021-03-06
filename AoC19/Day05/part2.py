def main():
    opcodes = list(map(int, input().split(',')))
    index = 0
    first_opcode = opcodes[index]

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
            opcodes[opcodes[index + 1]] = int(input())
            index += 2
        elif action == 4:
            print(opcodes[opcodes[index + 1]])
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

main()
