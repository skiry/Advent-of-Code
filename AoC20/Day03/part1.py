def main():
	trees = 0
	y = 0
	length = len(input())
	while True:
		try:
			line = input()
			y = (y + 3) % length
			if line[y] == '#':
				trees += 1
		except:
			return trees

print(main())
