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

grid = []
for _ in range(h):
    grid.append([0] * w)

for robot in robots:
    pos = robots[robot].get_position_at_n(100, h, w)
    grid[pos[1]][pos[0]] += 1

mid_x = w // 2
mid_y = h // 2


quad_a = 0
quad_b = 0
quad_c = 0
quad_d = 0
for line in grid[:mid_y]:
    quad_a += sum(line[:mid_x])
    quad_b += sum(line[mid_x + 1:])
for line in grid[mid_y + 1:]:
    quad_c += sum(line[:mid_x])
    quad_d += sum(line[mid_x + 1:])

for line in grid:
    print("".join([str(x) for x in line]))

print(quad_a * quad_b * quad_c * quad_d)