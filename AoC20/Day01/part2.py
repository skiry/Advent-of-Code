from collections import defaultdict

def main():
    numbersDict = defaultdict(int)
    numbersList = []
    while True:
            number = int(input())
            for x in numbersList:
                other = 2020 - number - x
                if (number ^ other ^ x) in [number, other, x]:
                    need = 2
                else:
                    need = 1
                if numbersDict[other] == need:
                    return other * number * x
            numbersDict[number] += 1
            numbersList.append(number)

print(main())
