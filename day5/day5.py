import math

def check_update(update, rules):
    update_parts = update.split(',')
    update_length = len(update_parts)
    for i in range(update_length - 1):
        for j in range(i + 1, update_length):
            expected_rule = update_parts[i] + '|' + update_parts[j]
            if expected_rule not in rules:
                return 0
    middle_index = math.floor(update_length/2)
    return int(update_parts[middle_index])




# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

split_index = lines.index('')

rules = lines[:split_index]
updates = lines[split_index + 1:]

answer = 0
for update in updates:
    answer += check_update(update, lines)

print(answer)
