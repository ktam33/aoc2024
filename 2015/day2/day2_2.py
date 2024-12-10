# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line for line in file]

answer = 0
for line in lines:
    nums = [int(x) for x in line.split('x')]
    nums.sort()
    answer += nums[0] * 2 + nums[1] * 2 + nums[0] * nums[1] * nums[2]
    
print(answer)