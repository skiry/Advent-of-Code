def main():
    opcodes = list(map(int, input().split(',')))
    opcodes[1] = 12
    opcodes[2] = 2
    index = 0
    first_opcode = opcodes[index]

    while first_opcode != 99:
        if first_opcode == 1:
            opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] + opcodes[opcodes[index + 2]]
        else:
            opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] * opcodes[opcodes[index + 2]]
        index += 4
        first_opcode = opcodes[index]

    return opcodes[0]

print(main())
