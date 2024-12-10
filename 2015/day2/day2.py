# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line for line in file]

answer = 0
for line in lines:
    nums = [int(x) for x in line.split('x')]
    sides = [nums[0] * nums[1], nums[0] * nums[2], nums[1] * nums[2]]
    sides.sort()
    answer += sides[0] * 3 + sides[1] * 2 + sides[2] * 2

print(answer)