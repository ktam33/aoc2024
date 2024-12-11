with open('input.txt', 'r') as file:
    lines = [line for line in file]
input = lines[0]

answer = 0
for i, char in enumerate(input):
    if char == '(':
        answer += 1
    if char == ')':
        answer -= 1
    if answer == -1:
        print(i + 1)
        break
