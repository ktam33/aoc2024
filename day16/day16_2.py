with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

unvisited = {}
visited = {}


class Node:
    def __init__(self, pos, grid):
        self.pos = pos
        self.dist = 1_000_000
        self.prev_pos = []
        self.neighbors = {}
        # don't add a neighbor that faces the opposite direction because
        # that is where we just came from
        dir = pos[2]
        if grid[pos[0]][pos[1] + 1] in '.E' and dir != '<':
            self.neighbors[(pos[0], pos[1] + 1, '>')] = self.calc_cost('>')
        if grid[pos[0]][pos[1] - 1] in '.E' and dir != '>':
            self.neighbors[(pos[0], pos[1] - 1, '<')] = self.calc_cost('<')
        if grid[pos[0] + 1][pos[1]] in '.E' and dir != '^':
            self.neighbors[(pos[0] + 1, pos[1], 'v')] = self.calc_cost('v')
        if grid[pos[0] - 1][pos[1]] in '.E' and dir != 'v':
            self.neighbors[(pos[0] - 1, pos[1], '^')] = self.calc_cost('^')

    def calc_cost(self, dir):
        if self.pos[2] == dir:
            return 1
        else:
            return 1001

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.pos == other.pos and self.dir == other.dir

    def __hash__(self):
        return hash(self.pos)

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'S':
            start_node = Node((i, j, '>'), lines)
            start_node.dist = 0
            unvisited[(i, j, '>')] = start_node
        elif char in 'E.':
            if char == 'E':
                goal = (i,j)
            unvisited[(i, j, '>')] = Node((i, j, '>'), lines)
            unvisited[(i, j, '<')] = Node((i, j, '<'), lines)
            unvisited[(i, j, '^')] = Node((i, j, '^'), lines)
            unvisited[(i, j, 'v')] = Node((i, j, 'v'), lines)

goal_reached = False
while not goal_reached:
# while(len(unvisited) > 0):
    curr = None
    for key in unvisited:
        if curr == None or unvisited[key].dist < curr.dist:
            curr = unvisited[key]
    
    for pos in curr.neighbors:
        dist = curr.neighbors[pos] + curr.dist
        if pos in unvisited:
            neighbor_node = unvisited[pos] 
            if neighbor_node.dist >= dist:
                neighbor_node.dist = dist
                neighbor_node.prev_pos.append(curr.pos)
                if (pos[0], pos[1]) == goal:
                    goal_node = neighbor_node
                    goal_reached = True   

    visited[curr.pos] = curr
    del unvisited[curr.pos]


print(goal_node.dist)

def get_path_nodes(node, path_nodes, visited):
    path_nodes.add((node.pos[0], node.pos[1]))
    for pos in node.prev_pos:
        get_path_nodes(visited[pos], path_nodes, visited)

path_nodes = set()
get_path_nodes(goal_node, path_nodes, visited)
print(len(path_nodes))