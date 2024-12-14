def extend_region(pos, lines, region, perimeter = 0):
    h = len(lines)
    w = len(lines[0])
    curr_value = lines[pos[0]][pos[1]]
    if region == None:
        region = set([pos])
    region.add(pos)

    if pos[0] == 0:
        perimeter += 1
    if pos[0] == h - 1:
        perimeter += 1
    if pos[1] == 0:
        perimeter += 1
    if pos[1] == w - 1:
        perimeter += 1
    if pos[0] > 0 and lines[pos[0] - 1][pos[1]] != curr_value:
        perimeter += 1
    if pos[0] < h - 1 and lines[pos[0] + 1][pos[1]] != curr_value:
        perimeter += 1
    if pos[1] > 0 and lines[pos[0]][pos[1] - 1] != curr_value:
        perimeter += 1
    if pos[1] < w - 1 and lines[pos[0]][pos[1] + 1] != curr_value:
        perimeter += 1

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

print(regions)

answer = 0
for region in regions:
    for entry in regions[region]:
        answer += len(entry[0]) * entry[1]

print(answer)
