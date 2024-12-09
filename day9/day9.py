from tqdm import tqdm
import itertools

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line for line in file]
input = lines[0]
disk = []
for i, char in enumerate(input):
    block_size = int(char)
    if i % 2 == 0:
        file_index = int(i/2)
        disk.extend([file_index] * block_size)
    else:
        disk.extend([None] * block_size)

i = 0
j = len(disk) - 1

while i < j:
    while disk[j] == None:
        j -= 1
    while disk[i] != None:
        i += 1
    
    disk[i] = disk[j]
    disk[j] = None

    i += 1
    j -= 1

i = 0
answer = 0
while disk[i] != None:
    answer += i * disk[i]
    i += 1

print(answer)