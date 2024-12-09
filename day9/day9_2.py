from tqdm import tqdm
import itertools



# Read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line for line in file]
input = lines[0]
disk = []
initial_files = []
free_blocks = []

curr_index = 0
for i, char in enumerate(input):
    block_size = int(char)
    if block_size > 0:
        end_index = curr_index + block_size - 1
        if i % 2 == 0:
            file_index = int(i/2)
            disk.extend([file_index] * block_size)
            initial_files.append((file_index, block_size, curr_index, end_index))
        else:
            disk.extend([None] * block_size)
            free_blocks.append((block_size, curr_index, end_index))
        curr_index = end_index + 1

# Try to move files starting at the end
for file in reversed(initial_files):
    free_block = None
    free_block_index = None
    # Starting from the front, try to find a free block
    for i, block in enumerate(free_blocks):
        # If we already are farther then the block we are trying to move then stop
        if block[1] >= file[2]:
            break
        # Stop if we find a block that is big enough
        if block[0] >= file[1]:
            free_block = block
            free_block_index = i
            break
    # If we found a free block, do the move and update the free block list
    if free_block != None:
        del free_blocks[free_block_index]
        diff = block[0] - file[1]
        if diff > 0:
            remaining_block = (diff, block[1] + file[1],  block[2])
            free_blocks.insert(free_block_index, remaining_block)
        for j in range(file[1]):
            disk[free_block[1] + j] = file[0]
            disk[file[2] + j] = None 
           
answer = 0
for i, block in enumerate(disk):
    if block != None:
        answer += i * block

print(answer)