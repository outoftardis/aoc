# day 2
import os

def intcode(program):
    instr_pointer = 0
    opcode = program[instr_pointer]
    while opcode != 99:
        if opcode == 1:
            program[program[instr_pointer + 3]] = program[program[instr_pointer + 1]] + program[program[instr_pointer + 2]]
        elif opcode == 2:
            program[program[instr_pointer + 3]] = program[program[instr_pointer + 1]] * program[program[instr_pointer + 2]]
        else:
            # print('Error!')
            break
        instr_pointer += 4
        opcode = program[instr_pointer]
    return program

def restore(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

def compile(program, noun, verb):
    program = restore(program, noun, verb)
    program = intcode(program)
    return program

# To complete the gravity assist, you need to determine what pair of inputs produces the output
def gravity_assist(program, output):

    for noun in range(100):
        for verb in range(100):
            program_test = program[:]
            result = compile(program_test, noun, verb)
            #print(result[0])
            if result[0] == output:
                return noun, verb
    return -1, -1

script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//002.txt', script_path)

with open(input_file, 'r') as f:
    program = f.read()

program = [int(i) for i in program.split(',')]

# first task

program_01 = program[:]
program_01 = compile(program_01, noun = 12, verb = 2)
print(program_01[0])

# second task

program_02 = program[:]
noun, verb = gravity_assist(program_02, 19690720)
print(100 * noun + verb)
