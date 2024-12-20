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
# pad grid to avoid having to deal with boundary conditions
for i, line in enumerate(grid):
    grid[i] = "#" + line + "#"
dim += 2
grid.insert(0, '#' * dim)
grid.append('#' * dim)

for line in grid:
    print(line)

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
i = 0
while (curr != end):
    next = take_step(curr, last, grid)
    i += 1
    path[next] = i
    last = curr
    curr = next

shortcuts = {}
cutoff = 100 if file.name == 'input.txt' else 10
for step in path:
    curr_val = path[step]
    possible_shortcuts = set([
        (step[0] - 2, step[1]),
        (step[0] - 1, step[1] - 1),
        (step[0] - 1, step[1] + 1),
        (step[0] + 2, step[1]),
        (step[0] + 1, step[1] + 1),
        (step[0] + 1, step[1] - 1),
        (step[0], step[1] - 2),
        (step[0], step[1] + 2),
    ])
    for ps in possible_shortcuts:
        if ps in path and path[ps] - curr_val >= cutoff + 2:
            if path[ps] - curr_val - 2 in shortcuts:
                shortcuts[path[ps] - curr_val - 2].add(ps)
            else:
                shortcuts[path[ps] - curr_val - 2] = set([ps])

answer = sum([len(shortcuts[k]) for k in shortcuts])
print(answer)

