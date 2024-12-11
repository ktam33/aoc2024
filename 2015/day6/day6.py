import re

def print_grid(grid):
    for i in range(len(grid[0])):
        print(''.join(grid[i]))


with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

grid = [["0"] * 100] * 100
print_grid(grid)

for line in lines:
    m = re.search(r'^[a-z ]+', line) 
    operation = m.group().strip() 
    points = re.findall(r'\d+,\d+', line) 

answer = 0



print(answer)