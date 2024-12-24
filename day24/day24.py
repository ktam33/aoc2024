import re

def do_operation(x, op, y):
    if op == 'AND':
        return x and y
    if op == 'OR':
        return x or y
    if op == 'XOR':
        return x ^ y
    

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]


wires = {}

for line in lines[:lines.index('')]:
    wires[line[0:3]] = bool(int(line[5]))
    
not_done = lines[lines.index('') + 1:]
while(len(not_done) > 0):
    still_not_done = []
    for line in not_done:
        match = re.match(r'(\w{3}) (AND|XOR|OR) (\w{3}) -> (\w{3})', line)
        if match and match.group(1) in wires and match.group(3) in wires:
            wires[match.group(4)] = do_operation(wires[match.group(1)], match.group(2), wires[match.group(3)])
        else:
            still_not_done.append(line)        
    not_done = still_not_done

z_keys = sorted([wire for wire in wires if wire[0] == 'z'], reverse=True)

bin_string = "".join([str(int(wires[k]))for k in z_keys])
print(int(bin_string, 2))

