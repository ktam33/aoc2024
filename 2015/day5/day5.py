import re

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

answer = 0
for line in lines:
    vowel_count = len(re.findall('[aeiou]', line))
    has_double = False
    has_forbidden = False
    for i in range(len(line) - 1):
        next_two = line[i:i+2]
        if next_two[0] == next_two[1]:
            has_double = True
        if next_two == "ab" or next_two == "cd" or next_two == "pq" or next_two == "xy" and not has_forbidden:
            has_forbidden = True

    if vowel_count >= 3 and has_double and not has_forbidden:
        answer += 1

print(answer)