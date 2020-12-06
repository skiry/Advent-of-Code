def main():
	sum = 0
	answers = set()
	while True:
		try:
			line = input()
			if not len(line):
				sum += len(answers)
				answers = set()
			else:
				for c in line:
					answers.add(c)
		except:
			return sum

print(main())
