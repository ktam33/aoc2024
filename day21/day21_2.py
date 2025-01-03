import functools
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

with open('input.txt', 'r') as file:
    combos = [line.strip() for line in file]

def get_path(start, end, hole):
    if start == end:
        return 'A'
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

def get_num_path(combo):
    hole = numpad['X']
    prev_paths = set()
    combo = 'A' + combo
    for i in range(len(combo) - 1):
        new_paths = set()
        new_sections = get_path(numpad[combo[i]], numpad[combo[i + 1]], hole)
        if len(prev_paths) == 0:
            new_paths = new_sections
        else:
            for path in prev_paths:
                for section in new_sections:
                    new_paths.add(path + section)
        prev_paths = new_paths

    return prev_paths

@functools.cache
def get_len(step, depth):
    if depth == 1:
        return 1
    min_len = None
    hole = dirpad['X']
    paths = get_path(dirpad[step[0]], dirpad[step[1]], hole)
    paths = ['A' + path for path in paths]
    for path in paths:
        total_len = 0
        for i in range(len(path) - 1):
            total_len += get_len(path[i:i + 2], depth - 1)
        if min_len is None:
            min_len = total_len
        elif total_len < min_len:
            min_len = total_len
    return min_len

def main():
    answer = 0
    depth = 26
    for combo in combos:
        paths = get_num_path(combo)
        min_len = None
        for path in paths:
            path = 'A' + path
            total_len = 0
            for i in range(len(path) - 1):
                total_len += get_len(path[i:i + 2], depth)
            if min_len is None:
                min_len = total_len
            elif total_len < min_len:
                min_len = total_len
        answer += min_len * int(combo[0:3])

    return answer

print(main())
