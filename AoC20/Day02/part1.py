def main():
	valid = 0
	while True:
		try:
			line = input().split(":")
			policy = line[0].split(" ")
			password = line[1]
			numbers = policy[0].split("-")
			start = int(numbers[0])
			end = int(numbers[1])
			letter = policy[1]
			if start <= password.count(letter) <= end:
				valid += 1
		except:
			return valid

print(main())

