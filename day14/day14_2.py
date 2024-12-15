import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

def count_longest_x(line):
    is_on_x = False
    count = 0
    longest = 0
    for char in line:
        if char == 'x':
            count += 1
            if longest < count:
                longest = count
            is_on_x = True
        else:
            if is_on_x:
                is_on_x = False
                count = 0
    return longest
            
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
while True:
    grid = []
    for _ in range(h):
        grid.append(['.'] * w)
    for robot in robots:
        pos = robots[robot].get_position_at_n(i, h, w)
        grid[pos[1]][pos[0]] = 'x'

    x_limit = 10
    should_show = False
    for line in grid:
        if count_longest_x(line) >= x_limit:
            should_show = True
            break
    if should_show:
        for line in grid:
            print("".join(line))
        print(i)
        input()
    if i % 1000 == 0:
        print(i)
    i = i + 1



