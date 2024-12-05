def is_xmas_at_loc(j, i, height, width, lines):
    if lines[j][i] != 'A':
        return False
    
    # check if we are too close to any edge
    if i == 0 or j == 0 or i == width - 1 or j == height - 1:
        return False
    
    # get both crosses starting from position j, i
    cross1 = lines[j + 1][i - 1] + lines[j][i] + lines[j - 1][i + 1]
    cross2 = lines[j - 1][i - 1] + lines[j][i] + lines[j + 1][i + 1]

    if ((cross1 == 'MAS' or cross1 == 'SAM') and
        (cross2 == 'MAS' or cross2 == 'SAM')):
        return True

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
width = len(lines[0])
height = len(lines)

answer = 0
for j in range(height):
    for i in range(width):
        if is_xmas_at_loc(j, i, height, width, lines):
            answer += 1

print(answer)


