import aoc_help as aoc


def count_slope(pattern, right, down):
    x = 0
    count = 0
    width = len(pattern[0])
    for line in pattern[down::down]:
        x = (x + right) % width
        if line[x] == "#":
            count += 1
    return count


def count_total(pattern, slopes):
    total = 1
    for (right, down) in slopes:
        total *= count_slope(pattern, right, down)
    return total


pattern = aoc.get_input('003')
pattern = pattern.split('\n')

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
print(count_total(pattern, slopes))
