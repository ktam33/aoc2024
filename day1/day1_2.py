left_numbers = []
right_numbers = []

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# for each line, get the id on the left and right side of the line
for line in lines:
    line_parts = line.split("   ")
    left_numbers.append(int(line_parts[0]))
    right_numbers.append(int(line_parts[1]))

# sort the left and right numbers
left_numbers.sort()
right_numbers.sort()


right_counts = {}

for number in right_numbers:
    if number not in right_counts:
        right_counts[number] = 1
    else:
        right_counts[number] = right_counts[number] + 1

answer=0

for number in left_numbers:
    if number in right_counts:
        answer = answer + (number * right_counts[number])

print(answer)