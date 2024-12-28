import re
from tqdm import tqdm

class Wire:
    def __init__(self, output, x, y, op):
        self.output = output
        self.x = x
        self.y = y
        self.op = op
        self.value = None

    def __repr__(self):
        if self.is_input():
            return f'{self.output} = {self.value}'
        else:
            return f'{self.x} {self.op} {self.y} -> {self.output}'

    def is_input(self):
        return self.op is None
    
    def __hash__(self):
        return hash((self.output, self.x, self.op, self.y))
    
    def __eq__(self, value):
        if not isinstance(value, Wire):
            return False
        return (
            self.output == value.output and 
            self.x == value.x and 
            self.y == value.y and 
            self.op == value.op
        )

def do_operation(x, op, y):
    if op == 'AND':
        return x and y
    if op == 'OR':
        return x or y
    if op == 'XOR':
        return x ^ y
    
def find_adder_wires(wire_num, wires, connected, show_results = True):
    wire_re = rf'[xyz]{wire_num}'
    for key in wires:
        wire = wires[key]
        if not wire.is_input() and (re.match(wire_re, wire.x) or re.match(wire_re, wire.y)):
            connected.add(wire)
            if wire_num != '00':
                connected.update(find_wire_with_input(wire.output, wires))
        elif re.match(wire_re, wire.output):
            connected.add(wire)
    
    c_out_dest = None
    c_out = None
    for c in connected:
        if c.op == 'OR':
            c_out = c
            c_out_dest = list(find_wire_with_input(c.output, wires, 'XOR'))

    if (
        c_out_dest is not None and (
            len(c_out_dest) != 1 or c_out_dest[0].output != f'z{(int(wire_num) + 1):02}'
        ) and
        wire_num != '44' and wire_num != '45'
    ):
        print('\n### ' + wire_num + ' ###\n')
        for c in connected:
            print(c)
        print(f'c_out: {c_out}')
        print(f'c_out destination: {c_out_dest}')
    
    print('\n### ' + wire_num + ' ###\n')
    for c in connected:
        print(c)
    print(f'c_out: {c_out}')
    print(f'c_out destination: {c_out_dest}')

def find_wire_with_input(input, wires, op = None):
    candidates = set()
    for key in wires:
        wire = wires[key]
        if wire.x == input or wire.y == input:
            if op == None:
                candidates.add(wire)
            elif op == wire.op:
                candidates.add(wire)
    return candidates



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

# Solved by printing out wires for each bit's adder circuit and manually 
# figuring out the swaps to untangle things. 
# TODO: figure out logic to solve this
# swaps = [('z09', 'gwh'), ('z21', 'rcb'), ('jct', 'z39'), ('wbw', 'wgb')]
# for swap in swaps:
#     swap_wires(swap, wires)

for i in range(46):
    find_adder_wires(f'{i:02}', wires, set())

results = get_test_results(wires)
print(results)

swaps_flattened = [item for swap in swaps for item in swap]
swaps_flattened.sort()
print(','.join(swaps_flattened))