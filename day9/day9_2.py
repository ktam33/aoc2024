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

        # this next part where we update the free block list to reflect the file we moved
        # is not really necessary to solve the problem

        # if moved file is ahead of all free blocks, just add the new free block
        if file[2] < free_blocks[0][1]:
            free_blocks.insert(0, (file[1], file[2], file[3]))
        else:
            # loop through the free blocks from the end and see where the new free block should be added
            for j in range(len(free_blocks) - 1, -1, -1):
                current_free_block = free_blocks[j]
                next_block_index = j + 1
                if free_blocks[j][2] < file[2]:
                    # if we need to merge with the previous free block, do that
                    if current_free_block[2] == file[2] - 1:
                        free_blocks[j] = (current_free_block[0] + file[1], current_free_block[1], current_free_block[2] + file[1])
                    # else add a new free block and keep track of where we are
                    else:
                        free_blocks.insert(j + 1, (file[1], file[2], file[3]))
                        next_block_index += 1
                    # check if we need to merge with the next free block
                    if next_block_index < len(free_blocks) and free_blocks[next_block_index][1] == file[3] + 1:
                        modified_block = free_blocks[next_block_index - 1]
                        next_block = free_blocks[next_block_index]
                        free_blocks[next_block_index - 1] = (modified_block[0] + next_block[0], modified_block[1], next_block[2])
                        del free_blocks[next_block_index]
                    # no need to keep looping if we have already handled the new free block
                    break

answer = 0
for i, block in enumerate(disk):
    if block != None:
        answer += i * block

print(free_blocks)
print(answer)