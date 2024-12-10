import re

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

answer = 0
# lines = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
# lines = ['zztdcqzqddaazdjp']
for line in lines:
    
    found_pair = None
    double = None

    has_pair = False
    for i in range(len(line) - 1):
        pair = line[i:i + 2]
        if line[:i].find(pair) > -1 or line[i + 2:].find(pair) > -1:
            has_pair = True
            found_pair = pair
            break

    has_double = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            has_double = True
            double = line[i:i+3]
            break
    
    print(f'{line}: pair: {found_pair}, double: {double}, answer = {has_pair and has_double}')

    if has_pair and has_double:
        answer += 1


print(answer)