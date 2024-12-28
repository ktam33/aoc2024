with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

keys = []
locks = []

len(lines)


for i in range(0, len(lines), 8):
    item = [0,0,0,0,0]
    for j in (range(1, 6)):
        line = lines[i + j]
        for k in range(len(line)):
            if line[k] == '#':
                item[k] += 1
    if lines[i] == '#####':
        locks.append(item)
    else:
        keys.append(item)

answer = 0
for lock in locks:
    for key in keys:
        if all([lock[i] + key[i] <= 5 for i in range(5)]):
            answer += 1

print(locks)
print(keys)
print(answer)