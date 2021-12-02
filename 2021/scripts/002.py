import aoc_help as aoc


# part 1
def calculate_position(directions):
    position = {"horizontal": 0, "depth": 0}
    for direction, distance in directions:
        if direction == "forward":
            position["horizontal"] += int(distance)
        elif direction == "up":
            position["depth"] -= int(distance)
        else:
            position["depth"] += int(distance)
    return position["depth"] * position ["horizontal"]


# part 2
def calculate_position_aimed(directions):
    position = {"horizontal": 0, "depth": 0, "aim": 0}
    for direction, distance in directions:
        if direction == "forward":
            position["horizontal"] += int(distance)
            position["depth"]  += position["aim"] * int(distance)
        elif direction == "up":
            position["aim"] -= int(distance)
        else: # down
            position["aim"] += int(distance)

    return position["depth"] * position ["horizontal"]


# read data

directions = aoc.get_input('002')
directions = directions.split('\n')
directions = [entry.split(' ') for entry in directions]

# part 1
print(calculate_position(directions))

# part 2
print(calculate_position_aimed(directions))