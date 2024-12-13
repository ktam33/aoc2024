import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

def find_solution(a, b, goal):
    for i in range(1, 101, 1):
        for j in range(1, 101, 1):
            if (i * a[0] + j * b[0], i * a[1] + j * b[1]) == goal:
                return (i, j)
    return None


answer = 0

for i in range(len(lines)):
    if i % 4 == 0:
        match = re.match(r'Button [A, B]: X\+(\d+), Y\+(\d+)', lines[i])
        a = (int(match.group(1)), int(match.group(2)))
        match = re.match(r'Button [A, B]: X\+(\d+), Y\+(\d+)', lines[i + 1])
        b = (int(match.group(1)), int(match.group(2)))
        match = re.match(r'Prize: X=(\d+), Y=(\d+)', lines[i + 2])
        goal = (int(match.group(1)), int(match.group(2)))

        solution = find_solution(a, b, goal)
        if solution:
            answer += solution[0] * 3 + solution[1]

print(answer)

