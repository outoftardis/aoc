# day 4

# How many different passwords within the range given in your puzzle input meet these criteria?

def get_range(s):
    p_range = s.split('-')
    p_range = [int(p) for p in p_range]
    return p_range[0], p_range[1]

def count_unique(s):
    return len(set(s))

def count_passwords(start, finish):
    count = 0
    passwords = []
    for word in range(start, finish):
        word = str(word)
        if count_unique(word) != 6:
            increase = True
            for i in range(5):
                increase = increase and word[i] <= word[i + 1]
            count += int(increase)
            if increase:
                passwords.append(word)
    return count, passwords

def check(word):
    i = 0
    pairs = False
    while i < 6:
        count = 1
        while i < 5 and word[i] == word[i + 1]:
            count += 1
            i += 1
        if count == 2:
            pairs = True
            break
        i += 1
    return pairs    

def filter_passwords(passwords):  
    passwords = [word for word in passwords if check(word)]
    return len(passwords), passwords



start, finish = get_range('359282-820401')

# task 1
n, passwords = count_passwords(start, finish)
print(n)

# task 2
m, passwords = filter_passwords(passwords)
print(m)
