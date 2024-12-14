import re

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

dict = {}


not_done = lines
while(len(not_done) > 0):
    still_not_done = []
    for line in not_done:
        match = re.match(r'^(\d+) -> ([a-z]+)$', line)
        if match:
            dict[match.group(2)] = int(match.group(1))
            continue

        match = re.match(r'^([a-z]+) -> ([a-z]+)$', line)
        if match:
            if match.group(1) in dict:
                dict[match.group(2)] = dict[match.group(1)]
            else:
                still_not_done.append(line)
            continue

        match = re.match(r'^([a-z]+) ([A-Z]+) ([a-z]+) -> ([a-z]+)$', line)
        if match:
            if match.group(1) in dict and match.group(3) in dict:
                if match.group(2) == "AND":
                    dict[match.group(4)] = dict[match.group(1)] & dict[match.group(3)]
                elif match.group(2) == "OR":
                    dict[match.group(4)] = dict[match.group(1)] | dict[match.group(3)]
            else:
                still_not_done.append(line)
            continue

        match = re.match(r'^1 AND ([a-z]+) -> ([a-z]+)$', line)
        if match:
            if match.group(1) in dict:
                dict[match.group(2)] = 1 & dict[match.group(1)]
            else:
                still_not_done.append(line)
            continue

        match = re.match(r'^([a-z]+) ([A-Z]+) (\d+) -> ([a-z]+)$', line)
        if match:
            if match.group(1) in dict:
                if match.group(2) == "LSHIFT":
                    dict[match.group(4)] = dict[match.group(1)] << int(match.group(3))
                if match.group(2) == "RSHIFT":
                    dict[match.group(4)] = dict[match.group(1)] >> int(match.group(3))
            else:
                still_not_done.append(line)
            continue

        match = re.match(r'^NOT ([a-z]+) -> ([a-z]+)$', line)
        if match:
            if match.group(1) in dict:
                dict[match.group(2)] = ~dict[match.group(1)] & 0xffff
            else:
                still_not_done.append(line)
            continue
    not_done = still_not_done
print(dict['a'])