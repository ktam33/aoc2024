def get_sides(region):
    """
    Calculates the number of sides in a given region

    region -- dictionary where the key is a tuple representing a position 
    and the value is a list of sides at that position that are part of 
    a side of the region
    """
    i_s = sorted([x[0]for x in region])
    j_s = sorted([x[1]for x in region])
    range_i = range(i_s[0], i_s[-1] + 1)
    range_j = range(j_s[0], j_s[-1] + 1)
    
    up_sides = 0
    down_sides = 0

    for i in range_i:
        on_up = False
        on_down = False
        for j in range_j:
            if (i,j) in region:
                if 'u' in region[(i,j)]:
                    if not on_up:
                        up_sides += 1
                    on_up = True
                else:
                    on_up = False
                if 'd' in region[(i,j)]:
                    if not on_down:
                        down_sides += 1
                    on_down = True
                else:
                    on_down = False
            else:
                on_up = False
                on_down = False

    left_sides = 0
    right_sides = 0
    
    for j in range_j:
        on_left = False
        on_right = False
        for i in range_i:
            if (i,j) in region:
                if 'l' in region[(i,j)]:
                    if not on_left:
                        left_sides += 1
                    on_left = True
                else:
                    on_left = False
                if 'r' in region[(i,j)]:
                    if not on_right:
                        right_sides += 1
                    on_right = True
                else:
                    on_right = False
            else:
                on_left = False
                on_right = False

    return left_sides + right_sides + up_sides + down_sides

def extend_region(pos, lines, region, perimeter = 0):
    h = len(lines)
    w = len(lines[0])
    sides = set()
    curr_value = lines[pos[0]][pos[1]]
   
    

    if pos[0] == 0 or (pos[0] > 0 and lines[pos[0] - 1][pos[1]] != curr_value):
        perimeter += 1
        sides.add('u')
    if pos[0] == h - 1 or (pos[0] < h - 1 and lines[pos[0] + 1][pos[1]] != curr_value):
        perimeter += 1
        sides.add('d')
    if pos[1] == 0 or (pos[1] > 0 and lines[pos[0]][pos[1] - 1] != curr_value):
        perimeter += 1
        sides.add('l')
    if pos[1] == w - 1 or (lines[pos[0]][pos[1] + 1] != curr_value):
        perimeter += 1
        sides.add('r')

    corners = 0
    if sides == set('ur') or sides == set('ul') or sides == 'dl' or sides == 'dr':
        corners = 1
    elif len(sides) == 3:
        corners = 2
    elif len(sides) == 4:
        corners = 4

    if region == None:
        region = {}
    region[pos] = sides

    if (
            pos[0] > 0 and
            (pos[0] - 1, pos[1]) not in region and
            lines[pos[0] - 1][pos[1]] == curr_value
        ):
        r_p = extend_region((pos[0] - 1, pos[1]), lines, region)
        region.update(r_p[0])
        perimeter += r_p[1]
    if (
            pos[0] < h - 1 and
            (pos[0] + 1, pos[1]) not in region and
            lines[pos[0] + 1][pos[1]] == curr_value
        ):
        r_p = extend_region((pos[0] + 1, pos[1]), lines, region)
        region.update(r_p[0])
        perimeter += r_p[1]
    if (
            pos[1] > 0 and
            (pos[0], pos[1] - 1) not in region and
            lines[pos[0]][pos[1] - 1] == curr_value
        ):
        r_p = extend_region((pos[0], pos[1] - 1), lines, region)
        region.update(r_p[0])
        perimeter += r_p[1]
    if (
            pos[1] < w - 1 and
            (pos[0], pos[1] + 1) not in region and
            lines[pos[0]][pos[1] + 1] == curr_value
        ):
        r_p = extend_region((pos[0], pos[1] + 1), lines, region)
        region.update(r_p[0])
        perimeter += r_p[1]
    return (region, perimeter)

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

seen_positions = set()
regions = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if (i,j) not in seen_positions:
            r_p = extend_region((i,j), lines, None)
            seen_positions.update(r_p[0])
            if char in regions:
                regions[char].append(r_p)
            else:
                regions[char] = [r_p]


answer = 0
for region in regions:
    for entry in regions[region]:
        area = len(entry[0])
        sides = get_sides(entry[0])
        print(f"{region}: area = {area}, sides = {sides}")
        answer += area * sides

print(answer)