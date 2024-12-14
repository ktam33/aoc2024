import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]



class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
    
    def __repr__(self):
        return f"{(self.pos, self.vel)}"
    
    def get_position_at_n(self, n, h, w):
        x = self.pos[0] + self.vel[0] * n
        y = self.pos[1] + self.vel[1] * n

        x = x % w
        y = y % h

        return (x, y)

# h = 7
# w = 11
h = 103
w = 101

robots = {}

for i, line in enumerate(lines):
    match = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
    pos = (int(match.group(1)), int(match.group(2)))
    vel = (int(match.group(3)), int(match.group(4)))
    robots[i] = Robot(pos, vel)

i = 0
filled_avg = (0, 0)
while True:
    grid = []
    for _ in range(h):
        grid.append(['.'] * w)
    for robot in robots:
        pos = robots[robot].get_position_at_n(i, h, w)
        grid[pos[1]][pos[0]] = 'x'
    i = i + 1
    filled = 0
    space_to_count = 15
    for ii, line in enumerate(grid):
        if ii < space_to_count:
            filled += line.count('x')

    if i > 50:
        curr_percent = filled/filled_avg[1]
        if curr_percent < 0.30 or curr_percent > 1.90:
            for line in grid:
                print("".join(line))
            print(i)
            input()
        if i % 1000 == 0:
            print(i)

    filled_avg = (i, (filled_avg[0] * filled_avg[1] + filled)/i)


