import aoc_help as aoc

numbers = aoc.get_input('009')
numbers = numbers.split('\n')
numbers = [int(n) for n in numbers]

len_prefix = 25


def find_remainders(report, total):
    return [total - entry for entry in report]


def find_two(report, total):
    remainders = find_remainders(report, total)

    entries = list(set(remainders).intersection(set(report)))
    return entries


def check(i, numbers):
    possible = numbers[i-len_prefix:i]
    return len(find_two(possible, numbers[i]))


def find_sequence(numbers, start, total):
    i = start
    acc = 0
    ok = True
    while ok:
        acc += numbers[i]
        i += 1
        ok = acc < total
    return acc > total, i

# part 1

ok = True
i = len_prefix
while ok:
    ok = check(i, numbers) != 0
    i += 1

invalid = numbers[i-1]
print(invalid)

# part 2
not_found = True
start = -1
while not_found:
    start += 1
    not_found, end = find_sequence(numbers, start, invalid)

print(start, end)

xmas_range = numbers[start:end]
weakness = min(xmas_range) + max(xmas_range)
print(weakness)