def main():
    fuel = 0
    while True:
        try:
            mass = int(input())
            while mass > 0:
                mass = mass // 3 - 2
                if mass > 0:
                    fuel += mass
        except Exception:
            break
    return fuel

print(main())

