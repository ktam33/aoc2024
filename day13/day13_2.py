import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

def find_solution(a, b, g):
    b_presses = (g[1] * a[0] - a[1] * g[0]) / (b[1] * a[0] - b[0] * a[1])
    a_presses = (g[0] - b[0] * b_presses) / a[0]
    if a_presses.is_integer() and b_presses.is_integer():
        return (a_presses, b_presses)
    else:
        return None

answer = 0
offset = 10000000000000
# offset = 0

for i in range(len(lines)):
    if i % 4 == 0:
        match = re.match(r'Button [A, B]: X\+(\d+), Y\+(\d+)', lines[i])
        a = (int(match.group(1)), int(match.group(2)))
        match = re.match(r'Button [A, B]: X\+(\d+), Y\+(\d+)', lines[i + 1])
        b = (int(match.group(1)), int(match.group(2)))
        match = re.match(r'Prize: X=(\d+), Y=(\d+)', lines[i + 2])
        goal = (int(match.group(1)) + offset, int(match.group(2)) + offset)

        solution = find_solution(a, b, goal)
        print(solution)
        if solution:
            answer += solution[0] * 3 + solution[1]

print(answer)

