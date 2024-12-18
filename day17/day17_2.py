import re

def get_combo(operand, registers):
    if operand >= 0 and operand <= 3:
        return operand
    if operand == 4:
        return registers['a']
    if operand == 5:
        return registers['b']
    if operand == 6:
        return registers['c']
    if operand == 7:
        raise Exception('combo operand 7 not implemented')


with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

registers = {}
registers['a'] = 0
registers['b'] = int(re.match(r'Register B: (\d+)', lines[1]).group(1))
registers['c'] = int(re.match(r'Register C: (\d+)', lines[2]).group(1))

init_b = registers['b']
init_c = registers['c']


program = [int(char) for char in lines[4][9:].split(',')]
output = []
current_a = 0
while output != program:
    current_a += 1
    print(current_a)
    registers['a'] += current_a
    registers['b'] = init_b
    registers['c'] = init_c
    output = []
    i = 0
    while i < len(program):
        instruction = program[i]
        operand = program[i + 1]

        if instruction == 0:
            registers['a'] = int(registers['a']/2 ** get_combo(operand, registers))
            i += 2
        elif instruction == 1:
            registers['b'] = registers['b'] ^ operand
            i += 2
        elif instruction == 2:
            registers['b'] = get_combo(operand, registers) % 8
            i += 2
        elif instruction == 3:
            if registers['a'] == 0:
                i += 2
            else:
                i = operand
        elif instruction == 4:
            registers['b'] = registers['b'] ^ registers['c']
            i += 2
        elif instruction == 5:
            output.append(get_combo(operand, registers) % 8)
            i += 2
        elif instruction == 6:
            registers['b'] = int(registers['a']/2 ** get_combo(operand, registers))
            i += 2
        elif instruction == 7:
            registers['c'] = int(registers['a']/2 ** get_combo(operand, registers))
            i += 2
    print(output)

print(current_a)