import aoc_help as aoc


codes = {"B": 1, "F": 0, "L": 0, "R": 1}


def into_binary(seat):
    return [codes[key] for key in list(seat)]


def parse(seat):
    return seat[:7], seat[7:]


def calculate(bin_code, num):
    start = 0
    end = num
    i = 0
    while start != end:
        code = bin_code[i]
        if code == 0:
            end = (end + start + 1) // 2 - 1
        else:
            start = (start + end + 1) // 2
        i += 1
    return start


def get_id(row, seat):
    return row * 8 + seat


seats = aoc.get_input('005')
seats = seats.split('\n')

# part 1

ids = []
for board_pass in seats:
    row, seat = parse(into_binary(board_pass))
    row = calculate(row, 127)
    seat = calculate(seat, 7)
    ids.append(get_id(row, seat))

print(max(ids))

# part 2

all = set(list(range(min(ids), max(ids))))
print(all.difference(ids))
