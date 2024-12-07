import math

def check_update(update_parts, rules):
    update_length = len(update_parts)
    for i in range(update_length - 1):
        for j in range(i + 1, update_length):
            expected_rule = update_parts[i] + '|' + update_parts[j]
            if expected_rule not in rules:
                return False
    return True

def reorder_update(update, rules):
    length = len(update)
    result = [None] * length
    for i in range(length):
        candidate = update[i]
        other_parts = update.copy()
        other_parts.pop(i)
        after_count = len([other for other in other_parts if candidate + "|" + other in rules])
        candidate_index = length - 1 - after_count 
        result[candidate_index] = candidate 
    return result


# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

split_index = lines.index('')

rules = lines[:split_index]
updates = lines[split_index + 1:]
updates = [update.split(',') for update in updates]

answer = 0
wrong_updates = [u for u in updates if not check_update(u, rules)]

for update in wrong_updates:
    reordered = reorder_update(update, rules)
    middle_index =  math.floor(len(reordered)/2)
    answer += int(reordered[middle_index])
print(answer)