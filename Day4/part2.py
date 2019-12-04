lower, upper = list(map(int, input().split('-')))

def is_valid(number):
    number_array = list(map(int, list(str(number))))
    six_digits = len(number_array) == 6
    same_adjacent = any(number_array[i] == number_array[i - 1] and \
                        (i - 2 < 0 or number_array[i] != number_array[i - 2]) and \
                        (i + 1 == len(number_array) or number_array[i] != number_array[i + 1]) \
                        for i in range(1, len(number_array)))
    monotonically_increasing = number_array == sorted(number_array)
    return six_digits and same_adjacent and monotonically_increasing

def count_numbers(lower, upper):
    counter = 0
    for number in range(lower, upper + 1):
        if is_valid(number):
            counter += 1
    return counter

print(count_numbers(lower, upper))