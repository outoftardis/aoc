import aoc_help as aoc


instructions = aoc.get_input('003')
instructions = list(instructions)
print(instructions)


directions = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}


def update_location(x, y, where):
    x_move, y_move = directions[where]
    return  x + x_move, y + y_move


def find_locations(instructions):
    x = 0
    y = 0
    locations = [(x, y)]
    for instruction in instructions:
        x, y = update_location(x, y, instruction)
        locations.append((x, y))
    return set(locations)

# part 1

print(len(find_locations(instructions)))

# part 2

santa = find_locations(instructions[::2])
robot = find_locations(instructions[1::2])
print(len(santa.union(robot)))