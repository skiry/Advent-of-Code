def main():
    numbers = set()
    while True:
            number = int(input())
            other = 2020 - number
            if other in numbers:
                return other * number
            numbers.add(number)

print(main())
