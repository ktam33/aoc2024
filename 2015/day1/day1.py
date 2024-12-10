with open('input.txt', 'r') as file:
    lines = [line for line in file]
input = lines[0]

answer = 0
for char in input:
    if char == '(':
        answer += 1
    if char == ')':
        answer -= 1

print(answer)