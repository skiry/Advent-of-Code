def main():
    pos = []
    s = set()
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    pos.append([int(x.split("=")[1]) for x in input().strip("<>").split(", ")])
    vel = [[0 for x in range(3)] for x in range(4)]

    for index in range(999999999):
        if str(pos) + str(vel) in s:
            return index
        s.add(str(pos) + str(vel))
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

print(main())