from tqdm import tqdm
from tqdm.contrib import itertools

class Day6Map:
    def __init__(self, lines):
        self.position = (None, None, None)
        self.height = len(lines)
        self.width = len(lines[0])
        self.obstacles = set()
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == '#':
                    self.obstacles.add((i, j))
                if char == "^" or char == "v" or char == "<" or char == ">":
                    self.position = (i, j, char)
        self.visited = set()
        self.start_position = self.position

    def reset(self):
        self.position = self.start_position
        self.visited = set()

    def is_loop(self):
        self.visited.add(self.position)
        while(not self._is_done()):
            next_step = self._get_next_step()
            if (next_step[0], next_step[1]) in self.obstacles:
                self._change_orientation()
            else:
                self.position = next_step
                if next_step in self.visited:
                    return True
                else:
                    self.visited.add(self.position)
        return False

    def _change_orientation(self):
        if self.position[2] == "^":
            self.position = (self.position[0], self.position[1], ">")
        elif self.position[2] == ">":
            self.position = (self.position[0], self.position[1], "v")
        elif self.position[2] == "v":
            self.position = (self.position[0], self.position[1], "<")
        elif self.position[2] == "<":
            self.position = (self.position[0], self.position[1], "^")

    def _get_next_step(self):
        next_step = (None, None, None)
        if self.position[2] == "^":
            next_step = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.position[2] == "v":
            next_step = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.position[2] == ">":
            next_step = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.position[2] == "<":
            next_step = (self.position[0], self.position[1] - 1, self.position[2])
        return next_step

    def _is_done(self):
        if self.position[0] == 0 and self.position[2] == "^":
            return True
        elif self.position[0] == self.height - 1 and self.position[2] == "v":
            return True
        elif self.position[1] == 0 and self.position[2] == "<":
            return True
        elif self.position[1] == self.width - 1 and self.position[2] == ">":
            return True
        return False

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = Day6Map(lines)
start_position = map.position

loop_count = 0

first_run_is_loop = map.is_loop()

obstacles_to_add = set()
for position in map.visited:
    obstacles_to_add.add((position[0], position[1]))
map.reset()

if not first_run_is_loop:
    for obstacle in tqdm(obstacles_to_add):
        if (obstacle[0], obstacle[1]) != (start_position[0], start_position[1]) and (obstacle[0], obstacle[1]) not in map.obstacles:
            map.obstacles.add((obstacle[0], obstacle[1]))
            if map.is_loop():
                loop_count += 1
            map.obstacles.remove((obstacle[0], obstacle[1]))
            map.reset()

print(loop_count)

