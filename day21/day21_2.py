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

dir_costs = {
    '<v': 1,
    '<>': 2,
    '<^': 2,
    '<A': 3,
    'v<': 1,
    'v>': 1,
    'v^': 1,
    'vA': 2,
    '><': 2,
    '>v': 1,
    '>^': 2,
    '>A': 1,
    '^<': 2,
    '^v': 1,
    '^>': 2,
    '^A': 1,
    'A^': 1,
    'Av': 2,
    'A>': 1,
    'A<': 3,
}

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

@functools.cache
def get_path(start, end, hole):
    i_move = 'v' if end[0] > start[0] else '^'
    j_move = '>' if end[1] > start[1] else '<'

    i_move = i_move * abs(end[0] - start[0])
    j_move = j_move * abs(end[1] - start[1])

    j_first = j_move + i_move + 'A'
    i_first = i_move + j_move + 'A'
    i_cost = get_path_cost('A' + i_first)
    j_cost = get_path_cost('A' + j_first)
    if start[1] == hole[1] and end[0] == hole[0]:
        return set([j_first])
    elif start[0] == hole[0] and end[1] == hole[1]:
        return set([i_first])
    elif i_cost > j_cost:
        return set([j_first])
    elif i_cost < j_cost:
        return set([i_first])
    else:
        return set([i_first, j_first])

@functools.cache
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
def get_dir_path(combo):
    hole = dirpad['X']
    prev_paths = set()
    combo = 'A' + combo
    for i in range(len(combo) - 1):
        new_paths = set()
        new_sections = get_path(dirpad[combo[i]], dirpad[combo[i + 1]], hole)
        if len(prev_paths) == 0:
            new_paths = new_sections
        else:
            for path in prev_paths:
                for section in new_sections:
                    new_paths.add(path + section)
        prev_paths = new_paths

    return prev_paths

@functools.cache
def get_path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        if path[i] == path[i + 1]:
            continue
        cost += dir_costs[path[i:i + 2]]
    return cost

def prune_paths(paths):
    print(f'starting number of paths: {len(paths)}')
    path_costs = {}
    min_cost = None
    # min_path = None
    for path in paths:
        cost = get_path_cost(path)
        path_costs[path] = cost
        if min_cost == None:
            min_cost = cost
            # min_path = path
        elif cost < min_cost:
            min_cost = cost
            # min_path = path
    pruned_paths = [path for path in path_costs if path_costs[path] == min_cost]
    # pruned_paths = [min_path]
    print(f'ending number of paths: {len(pruned_paths)}')
    return pruned_paths

# def get_cost(step, depth):
#     return 1


answer = 0
for combo in combos:
    paths = get_num_path(combo)
    paths = prune_paths(paths)
    print(combo)
    print(paths)

    # for path in paths:


    for _ in range(2):
        new_paths = set()
        for path in paths:
            new_paths.update(get_dir_path(path))
        paths = new_paths
        paths = prune_paths(paths)

    last_lengths = set()
    a_counts = set()
    for path in paths:
        last_lengths.add(len(path))
        a_counts.add(path.count('A'))

    answer += min(last_lengths) * int(combo[0:3])

print(answer)





