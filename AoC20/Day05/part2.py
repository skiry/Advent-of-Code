def main():
	maxSeat = 0
	seats = set()
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
			seats.add(f*8+l)
		except:
			for i in range(6, 127*8):
				if i not in seats and (i - 1) in seats and (i + 1) in seats:
					return i

print(main())

