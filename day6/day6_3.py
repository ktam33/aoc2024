# Implementation without Python classes to see if it is faster.
# Spoiler: it wasn't, speed improvements came with using a set 
# rather than a list to store obstacle points

from tqdm import tqdm
from tqdm.contrib import itertools

def is_done(position):
    if position[0] == 0 and position[2] == 'u':
        return True
    if position[0] == height - 1 and position[2] == 'd':
        return True
    if position[1] == 0 and position[2] == 'l':
        return True
    if position[1] == width - 1 and position[2] == 'r':
        return True
    return False

def get_next_position(position):
    if position[2] == 'u':
        return (position[0] - 1, position[1], position[2])
    if position[2] == 'r':
        return (position[0], position[1] + 1, position[2])
    if position[2] == 'd':
        return (position[0] + 1, position[1], position[2])
    if position[2] == 'l':
        return (position[0], position[1] - 1, position[2])

def turn(direction):
    if (direction == 'u'):
        return 'r'
    if (direction == 'r'):
        return 'd'
    if (direction == 'd'):
        return 'l'
    if (direction == 'l'):
        return 'u'

def is_loop(position, obstacles):
    seen = set()
    seen_spaces = set()

    seen.add(position)
    seen_spaces.add((position[0], position[1]))
    while not is_done(position):
        next = get_next_position(position)
        if ((next[0], next[1]) in obstacles):
            position = (position[0], position[1], turn(position[2]))
        else: 
            if next in seen:
                return (True, seen)
            position = next
            seen.add(position)
            seen_spaces.add((position[0], position[1]))

    return (False, seen_spaces)


with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

height = len(lines)
width = len(lines[0])
obstacles = set()

# 0 = up, 1 = right, 2 = down, 3 = left
start_position = (None, None, None)

for i in range(height):
    for j in range(width):
        if lines[i][j] == '^':
            start_position = (i, j, 'u')
        elif lines[i][j] == "#":
            obstacles.add((i, j))

# first_run = is_loop(start_position, obstacles)

# possible_obstacles = first_run[1]

# answer = 0

# for possible_obstacle in tqdm(possible_obstacles):
#     obstacles.add(possible_obstacle)
#     run = is_loop(start_position, obstacles)
#     if run[0]:
#         answer += 1
#     obstacles.remove(possible_obstacle)

answer = 0
for i, j in itertools.product(range(height), range(width)):
    if (i, j) not in obstacles and (i, j) != (start_position[0], start_position[1]):
        obstacles.add((i,j))
        run = is_loop(start_position, obstacles)
        if run[0]:
            answer += 1
        obstacles.remove((i,j))




print(answer)

