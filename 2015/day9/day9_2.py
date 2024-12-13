import re
import sys



with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

cities = {}

for line in lines:
    match = re.match(r"(\w+) to (\w+) = (\d+)", line)
    city_1 = match.group(1)
    city_2 = match.group(2)
    distance = match.group(3)
    if city_1 not in cities:
        cities[city_1] = {}
    if city_2 not in cities[city_1]:
        cities[city_1][city_2] = int(distance)

    if city_2 not in cities:
        cities[city_2] = {}
    if city_1 not in cities[city_2]:
        cities[city_2][city_1] = int(distance)

# from each city as the starting point, find the longest path to all cites
max_dist = 0

for city in cities:
    visited = set([city])
    next_city = None
    curr_city = city

    total = 0
    # from the current city, find the longest route to a city that hasn't been visited yet
    while len(visited) < len(cities):
        path = None
        for dest_city in cities[curr_city]:
            if dest_city not in visited:
                if path == None:
                    path = cities[curr_city][dest_city]
                    next_city = dest_city
                elif cities[curr_city][dest_city] > path:
                    path = cities[curr_city][dest_city]
                    next_city = dest_city
        total += path
        visited.add(next_city)
        curr_city = next_city

    if total > max_dist:
        max_dist = total
print(max_dist)
