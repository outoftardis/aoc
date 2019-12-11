# day 10

import os
import operator
import math

# not really an angle (k in y = kx + b line equation)
def get_angle(c1, c2):
    # c1 * x + c2 * y + c3 = 0 
    # y = - c3/c2 - c1/c2 * x
    if c2 != 0:
        return c1 / c2
    else:
        return math.inf

# line equations: for 2 points on the map we want to find a line that goes through both, then find all other asteroids that lay on the same line
# for second task: return a line slope as well
def get_line(a, b, astromap):
    # a: (x1, y1)
    # b: (x2, y2)
    # (y1 - y2) * x + (x2 - x1) * y + (x1 * y2 - x2 * y1) = 0
    # c1 * x + c2 * y + c3 = 0 // y = -c3/c2 - c1/c2 * x
    
    line = []
    
    c1 = a[1] - b[1]
    c2 = b[0] - a[0]
    c3 = a[0] * b[1] - b[0] * a[1]

    if c1 != 0 or c2 != 0:
        for astro in astromap:
            if astro[0] * c1 + astro[1] * c2 + c3 == 0:
                line.append(astro)

    return line, get_angle(c1, c2)

# sort asteroids on the line (based on distance from a given center)
def sort_points(line, center):
    # line - a list of tuples with coordinates
    dist = []
    
    for point in line:
        dist.append((point, ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)))
    
    dist = sorted(dist, key = lambda x: x[1])
    line = [item[0] for item in dist]

    return line

# order points on the line (left-to-rigt, right-to-left kind of order)
def order_points(line):
    # line - a list of tuples with coordinates
    line = sorted(line, key=lambda element: (element[0], element[1]))
    return line

# sort lines based on their slopes: from inf (vertical line) -> decreasing order
def sort_lines(astrolines):
    # coef k: point on this line
    astrolines = {k: v for k, v in sorted(astrolines.items(), key=lambda item: item[0], reverse = True)}
    return astrolines

# for each pair of asteroids on a line +1 to their count of # of asteroids they can see
def count_paired(line, counts):
    for i in range(len(line)-1):
        counts[line[i]] += 1
        counts[line[i+1]] += 1
    return counts

def clean(lines):
    return [line for line in lines if line != []]

# finding an order in which asteroids should be eliminated
def sort_firelines(firelines, station):
    first = []
    second = []
    for k, line in firelines.items():
        line = sort_points(line, station)
        if k == math.inf:
            # print('this is a vertical line')
            first.append([point for point in line if point[1] < station[1]])
            second.append([point for point in line if point[1] > station[1]])
        else:
            first.append([point for point in line if point[0] > station[0]])
            second.append([point for point in line if point[0] < station[0]])

    return clean(first) + clean(second)

# for the first task: 
def count_all_q(astromap):
    counts = {astro : 0 for astro in astromap}
    lines = []
    for asteroid in astromap:
        # print("checking: ", asteroid)
        others = astromap[:]
        others.remove(asteroid)
        other = others[0]

        while others:

            line = get_line(asteroid, other, astromap)[0]
            line = order_points(line)
            
            if line not in lines:
                lines.append(line)
                counts = count_paired(line, counts)

            for point in line:
                try:
                    others.remove(point)
                except:
                    pass
            try: 
                other = others[0]
            except:
                break
            
    return counts, lines

# slope: line (line is a list of asteroids)
def get_line_info(station, astromap):
    others = astromap[:]
    others.remove(station)
    other = others[0]
    lines = {}
    while others:
        line, k = get_line(station, other, astromap)

        if line not in lines.values():
            lines[k] = line

        for point in line:
            try:
                others.remove(point)
            except:
                pass
        try: 
            other = others[0]
        except:
            break
            
    return lines

# to get the order in which asteroids were destroyed
def exterminate(station, firelines):
    # takes a list from after sort_firelines
    lines = firelines[:]
    destroyed = []
    i = 0
    while True:
        while i < len(lines):
            line = lines[i]
            try:
                destroyed.append(line.pop(0))
                i += 1
            except:
                lines.pop(i)
        i = 0
        if len(lines) == 0:
            break
    return destroyed

# for task 2
def clear_space(station, astromap):

    firelines = get_line_info(station, astromap)
    firelines = sort_lines(firelines)
    firelines = sort_firelines(firelines, station)
    destroyed_asteroids = exterminate(station, firelines)

    return destroyed_asteroids


script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//010.txt', script_path)

astromap = []

with open(input_file, 'r') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        coords = [(x, i) for x, point in enumerate(line) if point == '#']
        astromap.extend(coords)

# astromap: coordinates of asteroids

# task 1
counts, astrolines = count_all_q(astromap)
astro_best = max(counts.items(), key=operator.itemgetter(1))
print(astro_best)

# task 2
station = astro_best[0]
destroyed_asteroids = clear_space(station, astromap)

ind = [1, 2, 3, 10, 20, 50, 100, 199, 200, 201, 299]
for i in ind:
    print(i, '\t',  destroyed_asteroids[i-1])

d = destroyed_asteroids[199]
print(100 * d[0] + d[1])