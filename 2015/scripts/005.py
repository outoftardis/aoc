import aoc_help as aoc
import re


def has_three_vowels(txt):
    return len(re.findall('[aeiou]', txt)) >= 3


def has_double_letters(txt):
    return bool(re.search(r'(.)\1', txt))


def does_not_contain_collocations(txt):
    return not bool(re.search('(ab|cd|pq|xy)', txt))


def check_niceness(txt):
    return has_three_vowels(txt) and has_double_letters(txt) and does_not_contain_collocations(txt)


def has_pair_non_overlapping_letters(txt):
    return bool(re.search(r'(..).*\1', txt))


def has_pair_same_letter_one_in_between(txt):
    return bool(re.search(r'(.).\1', txt))


def check_another_niceness(txt):
    return has_pair_non_overlapping_letters(txt) and has_pair_same_letter_one_in_between(txt)

lines = aoc.get_input('005')
lines = lines.split('\n')

# part 1
nice = [check_niceness(line) for line in lines]
print(sum(nice))

# part 2

another_nice = [check_another_niceness(line) for line in lines]
print(sum(another_nice))