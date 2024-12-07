def find_xmas_at_loc(j, i, height, width, lines):
    if lines[j][i] != 'X':
        return 0
    
    xmas_count = 0
    # check right
    if i + 3 < width and lines[j][i:(i + 4)] == 'XMAS':
        xmas_count += 1
    # check left
    if i - 3 >= 0 and lines[j][i] + lines[j][i - 1] + lines[j][i - 2] + lines[j][i - 3] == 'XMAS':
        xmas_count += 1
    # check up
    if j - 3 >= 0 and lines[j][i] + lines[j - 1][i] + lines[j - 2][i] + lines[j - 3][i] == 'XMAS':
        xmas_count += 1
    # check down
    if j + 3 < height and lines[j][i] + lines[j + 1][i] + lines[j + 2][i] + lines[j + 3][i] == 'XMAS':
        xmas_count += 1
    # check up and right
    if (j - 3 >= 0 and \
        i + 3 < width and \
        lines[j][i] + lines[j - 1][i + 1] + lines[j - 2][i + 2] + lines[j - 3][i + 3] == 'XMAS'):
        xmas_count += 1
    # check up and left
    if (j - 3 >= 0 and \
        i - 3 >= 0 and \
        lines[j][i] + lines[j - 1][i - 1] + lines[j - 2][i - 2] + lines[j - 3][i - 3] == 'XMAS'):
        xmas_count += 1
    # check down and right
    if (j + 3 < height and \
        i + 3 < width and \
        lines[j][i] + lines[j + 1][i + 1] + lines[j + 2][i + 2] + lines[j + 3][i + 3] == 'XMAS'):
        xmas_count += 1
    # check down and left   
    if (j + 3 < height and \
        i - 3 >= 0 and \
        lines[j][i] + lines[j + 1][i - 1] + lines[j + 2][i - 2] + lines[j + 3][i - 3] == 'XMAS'):
        xmas_count += 1

    return xmas_count
# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
width = len(lines[0])
height = len(lines)

answer = 0
for j in range(height):
    for i in range(width):
        answer += find_xmas_at_loc(j, i, height, width, lines)

# answer += find_xmas_at_loc(9,3,10,10,lines)

print(answer)


