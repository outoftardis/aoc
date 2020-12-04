import aoc_help as aoc

plan = aoc.get_input('001')
plan = list(plan)

# part one

plan = [-1 if i == ")" else 1 for i in plan]
print(sum(plan))

# part two
position = 0
for step, instruction in enumerate(plan):
    position += instruction
    if position == -1:
        break
print(step + 1)