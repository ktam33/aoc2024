from tqdm import tqdm
import itertools

def is_in_grid(node, h, w):
    return node[0] >= 0 and node[0] < h and node[1] >=0 and node[1] < w 

def find_antinodes(a, b, h, w):
    i_diff = b[0] - a[0]
    j_diff = b[1] - a[1]

    c = (b[0] + i_diff, b[1] + j_diff)
    d = (a[0] - i_diff, a[1] - j_diff)

    result = []
    if is_in_grid(c, h, w):
        result.append(c)
    if is_in_grid(d, h, w):
        result.append(d)

    return result

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

antennas = {}

height = len(lines)
width = len(lines[0])

for i in range(height):
    for j in range(width):
        current_char = lines[i][j]
        if current_char != '.':
            if current_char not in antennas:
                antennas[current_char] = set([(i, j)])
            else:
                antennas[current_char].add((i,j))

antinodes = set()
for antenna in tqdm(antennas):
    for pair in itertools.combinations(antennas[antenna], 2):
        antinodes.update(find_antinodes(pair[0], pair[1], height, width))


print(len(antinodes))