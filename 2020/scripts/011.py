import aoc_help as aoc
import numpy as np
import itertools

layout = aoc.get_input('011')
layout = layout.split('\n')


def generate_neighbors(x, y, n, m):
    x_coord = list(set([max(0, x - 1), x, min(x + 1, m -1)]))
    y_coord = list(set([max(0, y - 1), y, min(y + 1, n - 1)]))
    pairs = [(i, j) for i, j in itertools.product(x_coord, y_coord) if (i, j) != (x, y)]
    return pairs


def count_occupied(x, y, neighbors, ferry):
    occupied = 0
    for neighbor in neighbors:
        occupied += int(ferry[neighbor] == 1)
    return occupied


def step(ferry, n, m):
    updated_ferry = np.copy(ferry)
    for i in range(n):
        for j in range(m):
            if ferry[i][j] != -1:
                neighbors = generate_neighbors(i, j, n, m)
                occupied = count_occupied(i, j, neighbors, ferry)
                if ferry[i][j] == 0 and occupied == 0:
                    updated_ferry[i][j] = 1
                if ferry[i][j] ==1 and occupied >= 4:
                    updated_ferry[i][j] = 0
    return updated_ferry


def run(ferry, n, m):
    updated_ferry = step(ferry, n, m)
    if (updated_ferry == ferry).all():
        print(sum(sum(updated_ferry == 1)))
        return None
    else:
        run(updated_ferry, n, m)


# print(layout)
m = len(layout[0])
n = len(layout)
ferry = np.zeros((m, n), "int")

for i in range(n):
    ferry[i] = [-1 if s == "." else 0 for s in layout[i]]

run(ferry, n, m)