from tqdm import tqdm
import functools



with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

patterns = lines[0].split(', ')
@functools.cache
def find_pattern(line):
    matches = []
    for pattern in patterns:
        if line.startswith(pattern):
            rest_of_line = line[len(pattern):]
            if rest_of_line == '':
                matches.append((True, 1))
            else:
                matches.append(find_pattern(rest_of_line))
    if len(matches) == 0:
        return (False, 0)
    elif any([match[0] for match in matches]):
        total = sum([match[1] for match in matches if match[0] == True])
        return (True, total) 
    else:
        return (False, 0)

count = 0
answer = 0 
for line in tqdm(lines[2:]):
    result = find_pattern(line)
    # print(f'{line}: {result[1]}')
    if result[0]:
        count +=1
        answer += result[1]

print(count)
print(answer)