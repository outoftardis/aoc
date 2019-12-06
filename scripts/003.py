# day 3
import os

# What is the Manhattan distance from the central port to the closest intersection?

def split_wire(wire):
    return wire.split(',')

# adding all points in the right direction to the list of all coordinates
def add_path(start, direction, step):
    multiplier = {"D": -1, "U": 1, "L": -1, "R": 1}
    path = []
    if direction in ["D", "U"]: # second coordinate changes
        for i in range(step):
            path.append((start[0], start[1] + (i + 1) * multiplier[direction]))
    elif direction in ["R", "L"]: # first coordinate changes
        for i in range(step):
            path.append((start[0] + (i + 1) * multiplier[direction], start[1]))
    return path, path[-1]

# return a list of all points that a wire goes through
def get_coordinates(wire):
    start = (0, 0)
    coordinates = []
    for part in wire:
        direction = part[0] # D, L, R, U
        step = int(part[1:]) # how far in that direction?
        to_add, start = add_path(start, direction, step)
        coordinates.extend(to_add)
    return coordinates

# manhattan distance between point (a) and point (b) in 2d space
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# all interceptions of 2 sets of coordinates
def find_intercept(x, y):
    intercept = set(x).intersection(set(y))
    return list(intercept)

# find min of distances between (0, 0) and interception points
def find_min_dist(points):
    min_dist = manhattan(points[1], (0, 0))
    for point in points:
        dist = manhattan(point, (0, 0))
        min_dist = min(dist, min_dist)
    return min_dist

def find_closest(wires):
    coord_list = [get_coordinates(wire) for wire in wires]
    intercept_points = find_intercept(coord_list[0], coord_list[1])
    min_dist = find_min_dist(intercept_points)
    return min_dist
    
def count_steps(points, coord_list):
    steps = [0, 0]
    min_count = coord_list[0].index(points[0]) + coord_list[1].index(points[0]) + 2
    for point in points[1:]:
        for i, coords in enumerate(coord_list):
            steps[i] = coords.index(point) + 1
        min_count = min(min_count, steps[0] + steps[1])
    return min_count

def find_efficient(wires):
    coord_list = [get_coordinates(wire) for wire in wires]
    intercept_points = find_intercept(coord_list[0], coord_list[1])
    nsteps = count_steps(intercept_points, coord_list)
    return nsteps

script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//003.txt', script_path)

wires = []
with open(input_file, 'r') as f:
    for wire in f.readlines():
        wires.append(wire)

wires = [split_wire(wire) for wire in wires]

# task 1
print(find_closest(wires))

# task 2
print(find_efficient(wires))