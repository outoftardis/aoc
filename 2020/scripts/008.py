import aoc_help as aoc

instructions = aoc.get_input('008')
instructions = instructions.split('\n')
instructions = [instruction.split(' ') for instruction in instructions]

print(instructions)

def do_something(instruction, accumulator, i):
    action = instruction[0]
    delta = int(instruction[1])
    if action == "acc":
        accumulator += delta
        i += 1
    elif action == "jmp":
        i += delta
    else:
        i += 1
    return accumulator, i

# part 1

def break_cycle(instructions):
    no_repeats = True
    i = 0
    total = 0
    operations = []
    while no_repeats:
        # print(i)
        operations.append(i)
        instruction = instructions[i]
        total, i = do_something(instruction, total, i)
        no_repeats = i not in operations
    return total

print(break_cycle(instructions))


# part 2

def break_or_terminate(instructions):
    no_repeats = True
    i = 0
    total = 0
    operations = []
    n = len(instructions)
    while no_repeats:
        # print(i)
        operations.append(i)
        instruction = instructions[i]
        total, i = do_something(instruction, total, i)
        no_repeats = i not in operations
        if i == n:
            return total, i
    return total, i

print(instructions)
change = {"nop": "jmp", "jmp" : "nop"}
n_count = len(instructions)
for i in range(n_count):
    action = instructions[i][0]
    if action != "acc":
        # print("changing")
        instructions[i][0] = change[action]
        total, last_i = break_or_terminate(instructions)
        instructions[i][0] = change[change[action]]
        if last_i == n_count:
            print(total)
            break