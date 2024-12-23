#  +---+---+---+
#  | 7 | 8 | 9 |
#  +---+---+---+
#  | 4 | 5 | 6 |
#  +---+---+---+
#  | 1 | 2 | 3 |
#  +---+---+---+
#      | 0 | A |
#      +---+---+
# 
#      +---+---+
#      | ^ | A |
#  +---+---+---+
#  | < | v | > |
#  +---+---+---+

numpad = {
    '7': (0,0), 
    '8': (0,1), 
    '9': (0,2), 
    '4': (1,0), 
    '5': (1,1), 
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2), 
    'X': (3,0), 
    '0': (3,1), 
    'A': (3,2), 
    }
dirpad = {
    'X': (0,0), 
    '^': (0,1), 
    'A': (0,2), 
    '<': (1,0), 
    'v': (1,1), 
    '>': (1,2), 
}

with open('test_input.txt', 'r') as file:
    combos = [line.strip() for line in file]


def get_path(start, end, hole):
    i_move = 'v' if end[0] > start[0] else '^'
    j_move = '>' if end[1] > start[1] else '<'

    i_move = i_move * abs(end[0] - start[0])
    j_move = j_move * abs(end[1] - start[1])

    j_first = j_move + i_move + 'A'
    i_first = i_move + j_move + 'A'
    if start[1] == hole[1] and end[0] == hole[0]:
        return set([j_first])
    elif start[0] == hole[0] and end[1] == hole[1]:
        return set([i_first])
    else:
        return set([i_first, j_first])


def get_whole_path(combo, grid):
    hole = grid['X']
    prev_paths = set()
    combo = 'A' + combo
    for i in range(len(combo) - 1):
        new_paths = set()
        new_sections = get_path(grid[combo[i]], grid[combo[i + 1]], hole)
        if len(prev_paths) == 0:
            new_paths = new_sections
        else:
            for path in prev_paths:
                for section in new_sections:
                    new_paths.add(path + section)
        prev_paths = new_paths

    return prev_paths

def get_dir_path(prev):
    dirpad_hole = dirpad['X']
    path = ''
    prev = 'A' + prev
    for i in range(len(prev) - 1):
        path += get_path(dirpad[prev[i]], dirpad[prev[i + 1]], dirpad_hole )
    return path

answer = 0
for combo in combos:
    paths = get_whole_path(combo, numpad)
    print(combo)
    print(paths)
    paths_b = set()
    for path in paths:
        paths_b.update(get_whole_path(path, dirpad))
    # print(paths_b)

    paths_c = set()
    for path in paths_b:
        paths_c.update(get_whole_path(path, dirpad))
    # print(paths_c)
    last_lengths = set()
    for path in paths_c:
        last_lengths.add(len(path))

    print(min(last_lengths))
    answer += min(last_lengths) * int(combo[0:3])

print(answer)





