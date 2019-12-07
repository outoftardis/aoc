# day 5
import os

def parse_instruction(s):
    s = str(s)
    n = len(s)

    if n < 5:
        s = '0' * (5 - n) + s
    opcode = int(s[-2:])
    modes = [int(m) for m in s[0:-2][::-1]]

    return opcode, modes

def run_mode(mode, pointer, program):
    if mode == 0:
        return program[program[pointer]]
    elif mode == 1:
        return program[pointer]


def intcode(program, input_id):
    pointer = 0
    opcode, modes = parse_instruction(program[pointer])
    outputs = []
    while opcode != 99:
        if opcode == 1:
            program[program[pointer + 3]] = run_mode(modes[0], pointer + 1, program) + run_mode(modes[1], pointer + 2, program)
            move_pointer = 4
        elif opcode == 2:
            program[program[pointer + 3]] = run_mode(modes[0], pointer + 1, program) * run_mode(modes[1], pointer + 2, program)
            move_pointer = 4
        elif opcode == 3:
            program[program[pointer + 1]] = input_id
            move_pointer = 2
        elif opcode == 4:
            outputs.append(run_mode(modes[0], pointer + 1, program))
            move_pointer = 2
        elif opcode == 5:
            # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if run_mode(modes[0], pointer + 1, program) != 0:
                pointer = run_mode(modes[1], pointer + 2, program)
                move_pointer = 0
            else:
                move_pointer = 3
        elif opcode == 6:
            # if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if run_mode(modes[0], pointer + 1, program) == 0:
                pointer = run_mode(modes[1], pointer + 2, program)
                move_pointer = 0
            else:
                move_pointer = 3
        elif opcode == 7:
            # if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            program[program[pointer + 3]] = int(run_mode(modes[0], pointer + 1, program) < run_mode(modes[1], pointer + 2, program))
            move_pointer = 4
        elif opcode == 8:
            # if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
            program[program[pointer + 3]] = int(run_mode(modes[0], pointer + 1, program) == run_mode(modes[1], pointer + 2, program))
            move_pointer = 4
        else:
            return outputs

        if move_pointer != 0:
            pointer += move_pointer

        opcode, modes = parse_instruction(program[pointer])

    return outputs

def test(program, input_id):
    outputs = intcode(program, input_id)
    tested = outputs[1:-1]

    if tested == [int(i) for i in '0' * len(tested)]:
        print('Success')
    else:
        print('Error?')

    return outputs[-1]
        

script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//005.txt', script_path)

with open(input_file, 'r') as f:
    program = f.read()

program = [int(i) for i in program.split(',')]

# task 1
print(test(program[:], 1))

# task 3
print(test(program[:], 5))

