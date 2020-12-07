import aoc_help as aoc
import re
import numpy as np


def parse(line, actions):
    coordinates = re.findall('\d+,\d+', line)
    coordinates = [coordinate.split(',') for coordinate in coordinates]
    start = [int(coordinate) for coordinate in coordinates[0]]
    end = [int(coordinate) for coordinate in coordinates[1]]
    if "turn on" in line:
        action = actions[0]
    elif "turn off" in line:
        action = actions[1]
    elif "toggle" in line:
        action = actions[2]
    return action, start, end


def lit(instructions):
    grid = np.zeros((1000, 1000))
    for instruction in instructions:
        action, start, end = parse(instruction, [1, 0, -1])
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                state = int(grid[(i, j)])
                if state != action:
                    grid[(i, j)] = 1 - state
    return int(grid.sum())


def lit2(instructions):
    grid = np.zeros((1000, 1000))
    for instruction in instructions:
        action, start, end = parse(instruction, [1, -1, 2])
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                state = int(grid[(i, j)])
                grid[(i, j)] = max(state + action, 0)
    return int(grid.sum())

instructions = aoc.get_input('006')
instructions = instructions.split('\n')


# part 1
print(lit(instructions))

# part 2

print(lit2(instructions))
