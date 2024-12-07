import time

def is_done(position, h, w):
    if position[0] == 0 and direction == '^':
        return True
    if position[0] == h - 1 and direction == 'v':
        return True
    if position[1] == w - 1 and direction == '>':
        return True
    if position[1] == 0 and direction == '<':
        return True

def turn(direction):
    if direction == "^":
        return ">"
    if direction == ">":
        return "v"
    if direction == "v":
        return "<"
    if direction == "<":
        return "^"
    
def get_next_position(position, direction):
    if (direction == "^"):
        return (position[0] - 1, position[1])
    if (direction == ">"):
        return (position[0], position[1]+1)
    if (direction == "<"):
        return (position[0], position[1]- 1)
    if (direction == "v"):
        return (position[0] + 1, position[1])
    
     

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
h=len(lines)
w=len(lines[0])

pawns = set()
position = (None, None)
direction = None

visited = set()

for x in range(h):
    for y in range(w):
        if lines[x][y] == '#':
            pawns.add((x,y))
        if lines[x][y] == '^':
            position = (x,y)
            direction = '^'
        # print(f"{x}, {y}")

visited.add(position)
while(not is_done(position, h, w)):
    next_position = get_next_position(position, direction)
    if (next_position in pawns):
        direction = turn(direction)
    else:
        position = next_position    
        visited.add(position)
    print(position)
    print(direction)
    

print(len(visited))
        

