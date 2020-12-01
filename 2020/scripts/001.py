import aoc_help as aoc


def find_remainders(report, total = 2020):
    return [total - entry for entry in report]


def find_two(report, total = 2020):
    remainders = find_remainders(report, total)

    entries = list(set(remainders).intersection(set(report)))
    return entries


def find_three(report):
    result = []
    for entry in report:
        partial_entries = find_two(report, 2020 - entry)
        if len(partial_entries) == 2:
            result.append(entry)
    return result


# read input

report = aoc.get_input('001')
report = report.split('\n')
report = [int(entry) for entry in report]

# first part of the day

entries = find_two(report)
print(entries[0] * entries[1])

# second part of the day

result = find_three(report)
print(result[0] * result[1] * result [2])