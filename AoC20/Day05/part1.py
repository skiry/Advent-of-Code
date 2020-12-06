def main():
	maxSeat = 0
	while True:
		try:
			line = input()
			f, b = 0, 127
			for s in line[:7]:
				if s == 'F':
					b = (f + b) // 2
				else:
					f = (f + b) // 2 + 1
			l, r = 0, 7
			for s in line[7:]:
				if s == 'R':
					l = (l + r) // 2 + 1
				else:
					r = (l + r) // 2
			maxSeat = max(maxSeat, f * 8 + l)
		except:
			return maxSeat

print(main())
