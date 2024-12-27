import re
from tqdm import tqdm

class Wire:
    def __init__(self, output, x, y, op):
        self.output = output
        self.x = x
        self.y = y
        self.op = op
        self.value = None

    def is_input(self):
        return self.op is None

def do_operation(x, op, y):
    if op == 'AND':
        return x and y
    if op == 'OR':
        return x or y
    if op == 'XOR':
        return x ^ y
    
def get_combinations(seq):
    combinations = set()
    for i in range(0,len(seq)):
        for j in range(i+1,len(seq)):
            combinations.add((seq[i],seq[j]))
    return combinations

def calc_wires(wires):
    not_done = {k: v for k, v in wires.items() if v.value is None}
        
    while(len(not_done) > 0):
        start_size = len(not_done)
        still_not_done = {}
        for key in not_done:
            wire = not_done[key]
            if wires[wire.x].value is not None and wires[wire.y].value is not None:
                wire.value = do_operation(wires[wire.x].value, wire.op, wires[wire.y].value)
            else:
                still_not_done[key] = wire        
        not_done = still_not_done
        end_size = len(not_done)
        if start_size == end_size:
            break
    
    return len(not_done) == 0

def get_value_for(char, wires):
    keys = sorted([wire for wire in wires if wires[wire].output[0] == char], reverse=True)
    bin_string = "".join([str(int(wires[k].value))for k in keys])
    int_val = int(bin_string, 2)
    return bin_string, int_val

def set_value_for(char, bin_string, wires):
    length = len(bin_string)
    for i in range(length):
        index = char + f'{(length - 1 - i):02}' 
        wires[index].value = bool(int(bin_string[i]))

def get_bin_string(num, digits):
    return f'{bin(num)[2:]:>0{digits}}'

def find_first_mistake(expected, actual):
    first_mistake = -1
    for i in range(-1, -len(expected) - 1, -1):
        if actual[i] != expected[i] and abs(i) > first_mistake:
            first_mistake = abs(i)
            break
    return first_mistake

def get_test_results(wires):
    set_value_for('x', get_bin_string(35184372088831, 45), wires)
    set_value_for('y', get_bin_string(35184372088831, 45), wires)
    expected  = get_bin_string(35184372088831 + 35184372088831, 46)
    a = None
    b = None
    c = None
    reset_wires(wires)
    if calc_wires(wires):
        a = find_first_mistake(expected, get_value_for('z', wires)[0])

    set_value_for('x', get_bin_string(35184372088831, 45), wires)
    set_value_for('y', get_bin_string(0, 45), wires)
    expected  = get_bin_string(35184372088831, 46)
    
    reset_wires(wires)
    if calc_wires(wires):
        b = find_first_mistake(expected, get_value_for('z', wires)[0])

    set_value_for('x', get_bin_string(0, 45), wires)
    set_value_for('y', get_bin_string(35184372088831, 45), wires)
    
    reset_wires(wires)
    if calc_wires(wires):
        c = find_first_mistake(expected, get_value_for('z', wires)[0])

    return (a, b, c)

def reset_wires(wires):
    for wire in wires:
        if not wires[wire].is_input():
            wires[wire].value = None

def swap_wires(swap, wires):
    wire_1 = wires[swap[0]]
    wire_2 = wires[swap[1]]
    wire_1.output = swap[1]
    wire_2.output = swap[0]
    wires[swap[0]] = wire_2
    wires[swap[1]] = wire_1
    

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]


wires = {}

for line in lines[:lines.index('')]:
    input_wire = Wire(line[0:3], None, None, None)
    input_wire.value = bool(int(line[5]))
    wires[line[0:3]] = input_wire


for line in lines[lines.index('') + 1:]:
    match = re.match(r'(\w{3}) (AND|XOR|OR) (\w{3}) -> (\w{3})', line)
    wires[match.group(4)] = Wire(match.group(4), match.group(1), match.group(3), match.group(2))

swaps = set()
wires_to_swap = {k: v for k, v in wires.items() if not v.is_input()}
swaps = get_combinations(list(wires_to_swap.keys()))
x = get_value_for('x', wires)[1]
y = get_value_for('y', wires)[1]
expected  = get_bin_string(x + y, 46)



best_positions = get_test_results(wires)

# test
# reset_wires(wires)
# test_swaps = {('z34', 'rcb'), ('z38', 'z21'), ('z38', 'z45'), ('z34', 'z13')}
# for swap in test_swaps:
#     swap_wires(swap, wires)

# calc_wires(wires)
# test_mistake = find_first_mistake(expected, get_value_for('z', wires)[0])
#end test


best_swaps = set()
while(any(x != -1 for x in best_positions)):
    for swap in best_swaps:
        swap_wires(swap, wires)

    best_swap = None
    current_best_positions = best_positions
    for swap in tqdm(swaps.difference(best_swaps)):
        reset_wires(wires)
        swap_wires(swap, wires)
        
        new_positions = get_test_results(wires)
        if (
            all(x != None for x in new_positions) and (
                new_positions[0] > current_best_positions[0] or
                new_positions[1] > current_best_positions[1] or
                new_positions[2] > current_best_positions[2]
            )
        ):
            current_best_positions = new_positions
            best_swap = swap
        elif all(x != None and x == -1 for x in new_positions):
            current_best_positions = new_positions
            best_swap = swap
            break
        swap_wires(swap, wires)
    for swap in best_swaps:
        swap_wires(swap, wires)
    best_positions = current_best_positions
    if best_swap is None:
        raise Exception('no new swap found')
    best_swaps.add(best_swap)
    print(best_swaps)
    print(best_positions)
    # print(first_mistake)
    # print(swap)
print(best_swaps)
