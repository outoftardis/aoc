import aoc_help as aoc
from collections import Counter
import re


jolts = aoc.get_input('010')
jolts = jolts.split('\n')
jolts = [int(n) for n in jolts]
jolts.append(max(jolts) + 3)
jolts.append(0)
jolts = sorted(jolts)

print(jolts)

# part 1

diffs = []
for i in range(len(jolts) - 1):
    diffs.append(jolts[i+1] - jolts[i])
print(diffs)
diff_count = Counter(diffs)
print(diff_count)
print(diff_count[1] * diff_count[3])

# part 2

diffs = diffs[:-1]
print(diffs)
diffs = [str(i) for i in diffs]
diffs = "".join(diffs)
interchangable = re.findall(r"1{2,}", diffs)
print(interchangable)
interchangable = [2 ** (len(s) - 1) - ((len(s) - 1) // 3) for s in interchangable]
print(interchangable)

total = 1
for i in interchangable:
    total *= i
print(total)