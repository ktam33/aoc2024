import re

# read file contents into a list called lines
# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
input = ''.join(lines)

answer = 0
matches = re.findall(r'mul\(\d+\,\d+\)', input)
for match in matches:
    nums = [int(x) for x in match[4:-1].split(',')]
    answer += nums[0] * nums[1]

print(answer)
