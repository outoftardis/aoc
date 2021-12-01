import aoc_help as aoc


def analyze(report, report_range = 1):
    changes = []
    for index in range(report_range, len(report)):
        changes.append(report[index] - report[index - report_range])
    return changes


def check_increases(changes):
    return sum([change > 0 for change in changes])


# read data

report = aoc.get_input('001')
report = report.split('\n')
report = [int(entry) for entry in report]

# part 1
print(check_increases(analyze(report)))

# part 2
print(check_increases(analyze(report, report_range=3)))
