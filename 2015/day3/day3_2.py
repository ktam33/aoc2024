def move(location, direction):
    if direction == '>':
        location[0] += 1
    if direction == '<':
        location[0] -= 1
    if direction == '^':
        location[1] += 1
    if direction == 'v':
        location[1] -= 1


with open('input.txt', 'r') as file:
    lines = [line for line in file]

input = lines[0]
houses = set()
current_location = [0,0]
current_location_2 = [0,0]
houses.add((current_location[0], current_location[1]))
for i, char in enumerate(input):
    if i % 2 == 0:
        move(current_location, char)
        houses.add((current_location[0], current_location[1]))
    else:
        move(current_location_2, char)
        houses.add((current_location_2[0], current_location_2[1]))

print(len(houses))



