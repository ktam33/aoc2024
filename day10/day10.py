from tqdm import tqdm
import itertools

def take_step(position, grid, h, w):
    final_locations = set()
    position_value = grid[position[0]][position[1]]
    if position_value == 9:
        final_locations.add(position)
        return final_locations
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
    for step in next_steps:
        if grid[step[0]][step[1]] == position_value + 1:
            final_locations.update(take_step(step, grid, h, w))
    return final_locations

# Read file contents into a list called lines
with open('input.txt', 'r') as file:
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
            answer += len(take_step((y,x),grid, h, w))

print(answer)