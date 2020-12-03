import aoc_help as aoc

passwords = aoc.get_input('002')
passwords = passwords.split('\n')

policy = [item.split(":")[0].strip() for item in passwords]
passwords = [item.split(":")[1].strip() for item in passwords]

# part 1

total = 0
for i in range(len(passwords)):
    times = policy[i].split()[0].strip().split("-")
    letter = policy[i].split()[1].strip()
    passw = passwords[i]
    if int(times[0]) <= passw.count(letter) <= int(times[1]):
        total += 1

print(total)

# part 2

total = 0
for i in range(len(passwords)):
    times = policy[i].split()[0].strip().split("-")
    letter = policy[i].split()[1].strip()
    passw = passwords[i]
    freq = int(passw[int(times[0]) - 1] == letter) + int(passw[int(times[1]) - 1] == letter)
    if freq == 1:
        total += 1

print(total)