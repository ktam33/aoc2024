import math

def take_step(curr, last, grid):
    next = set([(curr[0] + 1, curr[1]),
                (curr[0] - 1, curr[1]), 
                (curr[0], curr[1] + 1),
                (curr[0], curr[1] - 1)])
    if last != None:
        next.remove(last)

    for pos in next:
        if grid[pos[0]][pos[1]] in 'E.':
            return pos

with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

dim = len(grid)
# pad grid by 19 spaces on each end to avoid having to deal with boundary conditions
for i, line in enumerate(grid):
    grid[i] = "#" * 19 + line + "#" * 19
dim += 19 * 2
for _ in range(19):
    grid.insert(0, '#' * dim)
    grid.append('#' * dim)

start = None
end = None
curr = None
last = None
path = {}

for i in range(dim):
    for j in range(dim):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)
            path[(i,j)] = -1
        elif grid[i][j] == '.':
            path[(i,j)] = -1

curr = start
path[start] = 0
i = 0
while (curr != end):
    next = take_step(curr, last, grid)
    i += 1
    path[next] = i
    last = curr
    curr = next

shortcuts = set()
cutoff = 100 if file.name == 'input.txt' else 50
for step in path:
    curr_val = path[step]
    possible_shortcuts = set()
    for i in range(-20, 21):
        for j in range(-(20 - abs(i)), (20 - abs(i)) + 1):
            possible_shortcuts.add(((step[0] + i, step[1] + j), abs(i) + abs(j)))



    for ps in possible_shortcuts:
        if ps[0] in path and path[ps[0]] - curr_val >= cutoff + ps[1]:
            shortcuts.add((step, ps[0], path[ps[0]] - curr_val - ps[1]))

answer = len(shortcuts)
print(answer)

# for sh in shortcuts:
#     print(f'start: {sh[0][0] - 19}, {sh[0][1] - 19}, end: {sh[1][0] - 19}, {sh[1][1] - 19}, length: {sh[2]}')
# input()

