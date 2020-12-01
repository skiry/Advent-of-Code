def main():
    fuel = 0
    while True:
        try:
            mass = int(input())
            fuel += mass // 3 - 2
        except Exception:
            break
    return fuel

print(main())

