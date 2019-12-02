TO_OBTAIN=19690720

def part1(opcodes, address1, address2):
    opcodes[1] = address1
    opcodes[2] = address2
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

def part2():
    opcodes = list(map(int, input().split(',')))
    i = 0
    j = 99
    while i <= j:
        result = part1(opcodes[:], i, j)
        if result == TO_OBTAIN:
            return 100 * i + j
        elif result > TO_OBTAIN:
            j -= 1
        else:
            i += 1
    i = 0
    j = 99
    while i <= j:
        result = part1(opcodes[:], j, i)
        if result == TO_OBTAIN:
            return 100 * j + i
        elif result > TO_OBTAIN:
            j -= 1
        else:
            i += 1
        
print(part2())
