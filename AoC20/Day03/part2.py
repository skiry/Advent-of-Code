import math

def main():
	y = [1, 3, 5, 7, 1]
	trees = [0] * 5
	currX = 0
	currY = [0] * 5
	length = len(input())
	while True:
		try:
			line = input()
			currX += 1
			for i in range(5):
				if i == 4 and currX % 2:
					continue
				currY[i] = (currY[i] + y[i]) % length
				if line[currY[i]] == '#':
					trees[i] += 1
		except:
			return math.prod(trees)

print(main())
