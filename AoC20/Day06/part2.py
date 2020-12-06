from collections import defaultdict

def main():
	sum = 0
	answers = defaultdict(int)
	people = 0
	while True:
		try:
			line = input()
			if not len(line):
				for c in range (ord('a'), ord('z') + 1):
					if answers[chr(c)] == people:
						sum += 1
				answers = defaultdict(int)
				people = 0
			else:
				people += 1
				for c in line:
					answers[c] += 1
		except:
			return sum

print(main())
