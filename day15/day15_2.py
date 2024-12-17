is_wide = False
with open('input.txt', 'r') as file:
    if 'wide' in file.name:
        is_wide = True
    lines = [line.strip() for line in file]

def print_grid(grid):
    for line in grid:
        print("".join(line))

def move(pos, dir, grid, h, w, do_move = True):
    curr = grid[pos[0]][pos[1]]
    if curr not in '@[]':
        raise Exception('Moving illegal character')
    # print(f'{curr}: {pos}, {dir}')
    # if requested to move out of the grid, return current position
    if ((dir == '>' and pos[1] == w - 1) or 
        (dir == '<' and pos[1] == 0) or
        (dir == 'v' and pos[0] == h - 1) or
        (dir == '^' and pos[0] == 0)):
        return pos
    if dir == '>':
        return move_horizontally(pos, dir, grid)
    elif dir == '<':
        return move_horizontally(pos, dir, grid)
    elif dir == 'v':
        return move_vertically(pos, dir, grid)
    elif dir == '^':
        return move_vertically(pos, dir, grid)

def move_horizontally(pos, dir, grid):
    next_pos = get_next(pos, dir)
    next = grid[next_pos[0]][next_pos[1]]
    if next == '.':
        return make_move(pos, dir, grid)
    elif next == '#':
        return pos
    elif next == '[' or next == ']':
        move_next = move(next_pos, dir, grid, h, w)
        if move_next != next_pos:
            return make_move(pos, dir, grid)
        else:
            return pos

def move_vertically(pos, dir, grid):
    next_pos = get_next(pos, dir)
    next = grid[next_pos[0]][next_pos[1]]
    if next == '.':
        return make_move(pos, dir, grid)
    elif '#' in next:
        return pos
    elif next == '[':
        pos_list = set([next_pos, get_next(next_pos, '>')])
        if move_all(pos_list, dir, grid):
            return make_move(pos, dir, grid)
        else:
            return pos
    elif next == ']':
        pos_list = set([next_pos, get_next(next_pos, '<')])
        if move_all(pos_list, dir, grid):
            return make_move(pos, dir, grid)
        else:
            return pos

def make_move(pos, dir, grid):
    curr = grid[pos[0]][pos[1]]
    new_pos = get_next(pos, dir)
    grid[new_pos[0]][new_pos[1]] = curr
    grid[pos[0]][pos[1]] = '.'
    return new_pos

def move_all(pos_list, dir, grid):
    next_pos_list = set()
    for pos in pos_list:
        next_pos= get_next(pos, dir)
        next_pos_value = grid[next_pos[0]][next_pos[1]]
        if next_pos_value == '#':
            return False
        elif next_pos_value == '.':
            pass
        elif next_pos_value == ']':
            next_pos_list.add(next_pos)
            next_pos_list.add(get_next(next_pos, '<'))
        elif next_pos_value == '[':
            next_pos_list.add(next_pos)
            next_pos_list.add(get_next(next_pos, '>'))
    if len(next_pos_list) == 0:
        for pos in pos_list:
            make_move(pos, dir, grid)
        return True
    else:
        if move_all(next_pos_list, dir, grid):
            for pos in pos_list:
                make_move(pos, dir, grid)
            return True
        else:
            return False

def get_next(pos, dir):
    if dir == '^':
        return (pos[0] - 1, pos[1])
    elif dir == 'v':
        return (pos[0] + 1, pos[1])
    elif dir == '>':
        return (pos[0], pos[1] + 1)
    elif dir == '<':
        return (pos[0], pos[1] - 1)

h = lines.index('')
input_w = len(lines[0])
robot = (0,0)
w = input_w * 2 if not is_wide else input_w
grid = [['.'] * w for _ in range(h)]
for i in range(h):
    for j in range(input_w):
        if not is_wide:
            if lines[i][j] == '.':
                grid[i][j * 2: j * 2 + 2] = ".."
            if lines[i][j] == '#':
                grid[i][j * 2: j * 2 + 2] = "##"
            if lines[i][j] == 'O':
                grid[i][j * 2: j * 2 + 2] = "[]"
            if lines[i][j] == '@':
                grid[i][j * 2: j * 2 + 2] = "@."
                robot = (i, j * 2)
        else:
            grid[i][j] = lines[i][j]
            if lines[i][j] == '@':
                robot = (i, j)
input_lines = []
for i in range(h + 1, len(lines)):
    input_lines.append(lines[i].strip())

inputs = "".join(input_lines)

# print_grid(grid)
for char in inputs:
    robot = move(robot, char, grid, h, w)
    # print_grid(grid)

answer = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == '[':
            answer += 100 * i + j

print_grid(grid)
print(answer)
