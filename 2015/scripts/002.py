import aoc_help as aoc
import itertools
import numpy as np


presents = aoc.get_input('002')
presents = presents.split('\n')
presents = [[int(measurement) for measurement in present.split('x')] for present in presents]

# part 1


def count_area(measurements):
    measurements.sort()
    area = 0
    area += measurements[0] * measurements[1]

    for i, j in itertools.combinations(measurements, 2):
        area += 2 * i * j

    return area


areas = [count_area(present) for present in presents]
print(sum(areas))

# part 2


def count_ribbon(measurements):
    measurements.sort()
    ribbon = 0
    ribbon += measurements[0] * 2 + measurements[1] * 2 + np.product(measurements)
    return ribbon


ribbons = [count_ribbon(present) for present in presents]
print(sum(ribbons))