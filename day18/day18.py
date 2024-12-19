def print_grid(grid):
    for line in grid:
        print("".join(line))

class Node:
    def __init__(self, pos, grid, w):
        self.pos = pos
        self.dist = 1_000_000
        self.init_dist = 1_000_000
        self.prev_pos = None
        self.neighbors = {}
        if pos[0] > 0 and grid[pos[0] - 1][pos[1]] in 'E.':
            self.neighbors[(pos[0] - 1, pos[1])] = 1
        if pos[0] < w - 1 and grid[pos[0] + 1][pos[1]] in 'E.':
            self.neighbors[(pos[0] + 1, pos[1])] = 1
        if pos[1] > 0 and grid[pos[0]][pos[1] - 1] in 'E.':
            self.neighbors[(pos[0], pos[1] - 1)] = 1
        if pos[1] < w - 1 and grid[pos[0]][pos[1] + 1] in 'E.':
            self.neighbors[(pos[0], pos[1] + 1)] = 1
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.pos == other.pos

    def __hash__(self):
        return hash((self.pos))

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

is_small = "test_" in file.name

w = 71 if not is_small else 7
num_bytes = 2961 if not is_small else 12

bytes = []
for line in lines:
    bytes.append((int(line.split(',')[0]), int(line.split(',')[1])))

grid = []
for i in range(w):
    grid.append(['.'] * w)

for byte in bytes[:num_bytes]:
    grid[byte[1]][byte[0]] = '#'

print(bytes[2960])

grid[0][0] = 'S'
grid[w - 1][w - 1] = 'E'

unvisited = {}
visited = {}

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == 'S':
            start_node = Node((i, j), grid, w)
            start_node.dist = 0
            unvisited[(i, j)] = start_node
        elif char in 'E.':
            if char == 'E':
                goal = (i,j)
            unvisited[(i, j)] = Node((i, j), grid, w)

goal_reached = False
goal_node = None
while(not goal_reached):
    curr = None
    for key in unvisited:
        if curr == None or unvisited[key].dist < curr.dist:
            curr = unvisited[key]
    if curr.dist == curr.init_dist:
        print('goal not reachable')
        break

    for pos in curr.neighbors:
        dist = curr.neighbors[pos] + curr.dist
        if pos in unvisited:
            neighbor_node = unvisited[pos]
            if neighbor_node.dist > dist:
                neighbor_node.dist = dist
                neighbor_node.previous_pos = curr.pos
                if (pos[0], pos[1]) == goal:
                    goal_node = neighbor_node
                    goal_reached = True

    visited[curr.pos] = curr
    del unvisited[curr.pos]
    if len(unvisited) == 0:
        print('no more unvisited nodes')
        break

if goal_node != None:
    print(goal_node.dist)