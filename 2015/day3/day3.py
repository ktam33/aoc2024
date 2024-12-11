with open('input.txt', 'r') as file:
    lines = [line for line in file]

input = lines[0]
houses = set()
current_location = [0,0]
houses.add((current_location[0], current_location[1]))
for char in input:
    if char == '>':
        current_location[0] += 1
    if char == '<':
        current_location[0] -= 1
    if char == '^':
        current_location[1] += 1
    if char == 'v':
        current_location[1] -= 1
    houses.add((current_location[0], current_location[1]))

print(len(houses))



