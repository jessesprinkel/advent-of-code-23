# Part 1

lottery_dict = {}
with open('input/day4.txt') as f:

    for line in f.readlines():
        numbers_dict = {
            'my_numbers': line.split(':')[1].split('|')[0].split(),
            'winning_numbers': line.split(':')[1].split('|')[1].split()
        }
        lottery_dict[line.split(':')[0]] = numbers_dict

total_points = 0
for k, v in lottery_dict.items():
    my_winning_numbers = list(set(v['my_numbers']) & set(v['winning_numbers']))

    v['my_wins'] = my_winning_numbers
    v['my_score'] = 2**(len(my_winning_numbers) - 1)

    total_points += 2**(len(my_winning_numbers) - 1) if my_winning_numbers else 0

print(f'Part 1: the total points for the scratch card pile is {total_points}')

# Part 2
lottery_dict = {}
with open('input/day4.txt') as f:

    for line in f.readlines():
        numbers_dict = {
            'my_numbers': line.split(':')[1].split('|')[0].split(),
            'winning_numbers': line.split(':')[1].split('|')[1].split(),
            'copies': 0
        }
        lottery_dict[line.split(':')[0]] = numbers_dict

total_points = 0
for k, v in lottery_dict.items():
    for _ in range(0, v['copies'] + 1):
        my_winning_numbers = list(set(v['my_numbers']) & set(v['winning_numbers']))
        if my_winning_numbers:
            for i in range(0, len(my_winning_numbers)):
                card_number = str((i + 1) + int(k.split()[1]))
                lottery_dict[f"Card{' ' * (4 - len(card_number))}{card_number}"]['copies'] += 1
                stop = 1
    

for k, v in lottery_dict.items():
    total_points += v['copies'] + 1

print(f'Part 2: there are {total_points} total scratchcards')
