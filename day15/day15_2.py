with open('test_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

def print_grid(grid):
    for line in grid:
        print("".join(line))

def move(pos, dir, grid, h, w):
    curr = grid[pos[0]][pos[1]]
    print(f'{curr}: {pos}, {dir}')
    if ((dir == '>' and pos[1] == w - 1) or 
        (dir == '<' and pos[1] == 0) or
        (dir == 'v' and pos[0] == h - 1) or
        (dir == '^' and pos[0] == 0)):
        return pos
    if dir == '>':
        next = grid[pos[0]][pos[1] + 1]
        if next == '.':
            grid[pos[0]][pos[1] + 1] = curr
            grid[pos[0]][pos[1]] = '.'
            return (pos[0], pos[1] + 1)
        elif next == '#':
            return pos
        elif next == 'O':
            move_next = move((pos[0], pos[1] + 1), dir, grid, h, w)
            if move_next != (pos[0], pos[1] + 1):
                grid[pos[0]][pos[1] + 1] = curr
                grid[pos[0]][pos[1]] = '.'
                return (pos[0], pos[1] + 1)
            else:
                return pos
    elif dir == '<': 
        next = grid[pos[0]][pos[1] - 1]
        if next == '.':
            grid[pos[0]][pos[1] - 1] = curr
            grid[pos[0]][pos[1]] = '.'
            return (pos[0], pos[1] - 1)
        elif next == '#':
            return pos
        elif next == 'O':
            move_next = move((pos[0], pos[1] - 1), dir, grid, h, w)
            if move_next != (pos[0], pos[1] - 1):
                grid[pos[0]][pos[1] - 1] = curr
                grid[pos[0]][pos[1]] = '.'
                return (pos[0], pos[1] - 1)
            else:
                return pos
    elif dir == 'v':
        next = grid[pos[0] + 1][pos[1]]
        if next == '.':
            grid[pos[0] + 1][pos[1]] = curr
            grid[pos[0]][pos[1]] = '.'
            return (pos[0] + 1, pos[1])
        elif next == '#':
            return pos
        elif next == 'O':
            move_next = move((pos[0] + 1, pos[1]), dir, grid, h, w)
            if move_next != (pos[0] + 1, pos[1]):
                grid[pos[0] + 1][pos[1]] = curr
                grid[pos[0]][pos[1]] = '.'
                return (pos[0] + 1, pos[1])
            else:
                return pos
    elif dir == '^':
        next = grid[pos[0] - 1][pos[1]]
        if next == '.':
            grid[pos[0] - 1][pos[1]] = curr
            grid[pos[0]][pos[1]] = '.'
            return (pos[0] - 1, pos[1])
        elif next == '#':
            return pos
        elif next == 'O':
            move_next = move((pos[0] - 1, pos[1]), dir, grid, h, w)
            if move_next != (pos[0] - 1, pos[1]):
                grid[pos[0] - 1][pos[1]] = curr
                grid[pos[0]][pos[1]] = '.'
                return (pos[0] - 1, pos[1])
            else:
                return pos
            

h = lines.index('')
w = len(lines[0]) * 2
robot = (0,0)
grid = [['.'] * w for _ in range(h)]
for i in range(h):
    for j in range(int(w/2)):
        if lines[i][j] == '.':
            grid[i][j * 2: j * 2 + 2] = ".."
        if lines[i][j] == '#':
            grid[i][j * 2: j * 2 + 2] = "##"
        if lines[i][j] == 'O':
            grid[i][j * 2: j * 2 + 2] = "[]"
        if lines[i][j] == '@':
            grid[i][j * 2: j * 2 + 2] = "@."
            robot = (i, j * 2)

input_lines = []
for i in range(h + 1, len(lines)):
    input_lines.append(lines[i].strip())

input = "".join(input_lines)

# for char in input:
#     robot = move(robot, char, grid, h, w)

answer = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'O':
            answer += 100 * i + j

print_grid(grid)
print(answer)
