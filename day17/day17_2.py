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
registers['b'] = 0
registers['c'] = 0

init_b = registers['b']
init_c = registers['c']

excluded = set([0])
program = [int(char) for char in lines[4][9:].split(',')]
found_answer = False
while not found_answer:
    current_start = 0
    for i in range(len(program)):
        program_section = program[-(i + 1):]
        print(program_section)
        output = []
        current_end = current_start + 8

        found_next = False
        for a in range(current_start,current_end):
            registers['a'] = a
            registers['b'] = 0
            registers['c'] = 0
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
            if output == program_section and a not in excluded:
                print(f"found a = {a} produces {output}")
                if len(program_section) == len(program):
                    found_answer = True
                current_start = a * 8
                found_next = True
                break
        if not found_next:
            excluded.add(current_start / 8)
            break