def main():
    pos = []
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    vel = [[0 for x in range(3)] for x in range(4)]

    for _ in range(1000):
        for i in range(4):
            for j in range(i + 1, 4):
                for k in range(3):
                    if pos[i][k] < pos[j][k]:
                        vel[i][k] += 1
                        vel[j][k] -= 1
                    elif pos[i][k] > pos[j][k]:
                        vel[i][k] -= 1
                        vel[j][k] += 1
        for i in range(4):
            for k in range(3):
                pos[i][k] += vel[i][k]

    res = 0
    for i in range(4):
        pot = 0
        kin = 0
        for k in range(3):
            pot += abs(pos[i][k])
            kin += abs(vel[i][k])
        res += pot * kin
    return res

print(main())