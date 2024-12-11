from tqdm import tqdm
import itertools

def take_step(position, grid, h, w):
    position_value = grid[position[0]][position[1]]
    if position_value == 9:
        return 1
    next_steps = []
    if position[0] > 0:
        next_steps.append((position[0] - 1, position[1]))
    if position[0] < h - 1:
        next_steps.append((position[0] + 1, position[1]))
    if position[1] > 0:
        next_steps.append((position[0], position[1] - 1))
    if position[1] < w - 1:
        next_steps.append((position[0], position[1] + 1))

    total = 0
    has_next = False
    for step in next_steps:
        if grid[step[0]][step[1]] == position_value + 1:
            if has_next == False:
                has_next = True
            total += take_step(step, grid, h, w)
    if has_next == False:
        return 0
    return total

# Read file contents into a list called lines
with open('test_input.txt', 'r') as file:
    lines = [line.strip() for line in file]
h = len(lines)
w = len(lines[0])

grid = []
for line in lines:
    grid.append([int(char) for char in line])

answer = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == 0:
            print(f"{y}, {x}")
            print(take_step((y, x), grid, h, w))

# print(take_step((0,4),grid, h, w))
