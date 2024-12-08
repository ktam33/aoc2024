from tqdm import tqdm
import itertools
import math

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

answers = []
numbers = []

for line in lines:
    line_parts = line.split(': ')
    answers.append(int(line_parts[0]))
    numbers.append([int(x) for x in line_parts[1].split(' ')])

result = 0
for i, total in (enumerate(tqdm(answers))):
    o = [['+', '*', '||']] * (len(numbers[i]) - 1)
    operators_list = list(itertools.product(*o))
    for operators in operators_list:
        total = numbers[i][0]
        for j in range(len(numbers[i]) - 1):
            next_num = numbers[i][j + 1]
            if operators[j] == '+':
                total += next_num
            elif operators[j] == '*':
                total *= next_num
            elif operators[j] == '||':
                # total = int(str(total) + str(numbers[i][j + 1]))
                total = total * (10 ** (int(math.log10(next_num)) + 1)) + next_num
        if total == answers[i]:
            result += total
            break

print(result)