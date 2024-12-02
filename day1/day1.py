left_numbers = []
right_numbers = []

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# for each line, get the id on the left and right side of the line
for line in lines:
    left_numbers.append(int(line[0:5]))
    right_numbers.append(int(line[8:13]))

# sort the left and right numbers
left_numbers.sort()
right_numbers.sort()

# calculate the difference between the right and left numbers
# and add up the differences in the answer variable
answer = 0 
for i in range(len(left_numbers)):
    diff = abs(right_numbers[i] - left_numbers[i])
    answer += diff

# show the final answer
print(answer)