import re

def print_grid(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))


with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

grid_size = 1000
grid = []
for i in range(grid_size):
    grid.append([0] * grid_size)

for line in lines:
    m = re.search(r'^[a-z ]+', line) 
    operation = m.group().strip() 
    points_match = re.findall(r'\d+,\d+', line) 
    point_a = [int(x) for x in points_match[0].split(',')]
    point_b = [int(x) for x in points_match[1].split(',')]
    for i in range(point_a[0], point_b[0] + 1):
        for j in range(point_a[1], point_b[1] + 1):
            if operation == "turn on":
                grid[i][j] += 1
            elif operation == "turn off":
                if grid[i][j] > 0:
                    grid[i][j] -= 1
            elif operation == "toggle":
                grid[i][j] += 2

print(sum([sum(line) for line in grid]))

