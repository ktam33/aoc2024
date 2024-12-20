from tqdm import tqdm
import functools



with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

patterns = lines[0].split(', ')
@functools.cache
def find_pattern(line):
    # print(line)
    matches = []
    for pattern in patterns:
        if line.startswith(pattern):
            rest_of_line = line[len(pattern):]
            if rest_of_line == '':
                return True
            else:
                matches.append(find_pattern(rest_of_line))
    if len(matches) == 0:
        return False
    elif any(matches):
        return True
    else:
        return False

count = 0
for line in tqdm(lines[2:]):
    if find_pattern(line):
        count +=1

print(count)