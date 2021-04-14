import aoc_help as aoc
import numpy as np
import itertools

instructions = aoc.get_input('012')
instructions = instructions.split('\n')

"""
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
"""

instructions = [(inst[0], int(inst[1:])) for inst in instructions]
# print(instructions)


def move(direction, value, x, y):
    if direction == "N":
        y += value
    elif direction == "S":
        y -= value
    elif direction == "E":
        x += value
    elif direction == "W":
        x -= value
    return x, y


orientation = {0: "E", 90: "N", 180: "W", 270: "S"}

degrees = 0
x = 0
y = 0
for direction, value in instructions:
    if direction in "NSWE":
        x, y = move(direction, value, x, y)
    elif direction == "F":
        x, y = move(orientation[degrees], value, x, y)
    elif direction == "R":
        degrees -= value
    elif direction == "L":
        degrees += value
    if degrees < 0:
        degrees = 360 + degrees
    elif degrees >= 360:
        degrees = degrees % 360
    # print(x, y)

manhatten = abs(x) + abs(y)
print(manhatten)