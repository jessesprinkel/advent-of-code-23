
# Part one
digits = []

with open('input/day1_p1.txt') as f:

    for line in f.readlines():
        all_digits = []
        for char in line:
            if char.isnumeric():
                all_digits.append(char)

        combined_first_last_dig = all_digits[0] + all_digits[-1]

        digits.append(int(combined_first_last_dig))

print(f'part 1: {sum(digits)}')


# Part two
digits = []
all_numbers = [('1', 'one'), ('2','two'),('3','three'),('4','four'),('5','five'),('6','six'),
               ('7','seven'),('8','eight'),('9','nine')]

with open('input/day1_p1.txt') as f:

    for line in f.readlines():

        all_digits = []

        # Get numeric numbers
        for i, char in enumerate(line):
            if char.isnumeric():
                all_digits.append((char, i))

        # Get string numbers
        for num in all_numbers:
            i = 0
            while line.find(num[1], i) != -1:
                all_digits.append((num[0], line.find(num[1], i)))
                i = line.find(num[1], i) + 1

        # Sort and concatenate numbers
        all_digits_sorted = sorted(all_digits, key = lambda x: x[1])
        combined_first_last_dig = all_digits_sorted[0][0] + all_digits_sorted[-1][0]

        digits.append(int(combined_first_last_dig))

print(f'part 2: {sum(digits)}')






