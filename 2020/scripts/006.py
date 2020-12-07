import aoc_help as aoc
import re
import functools


forms = aoc.get_input('006')
forms = forms.split('\n\n')

# part 1

forms_anyone = [re.sub('\n', '', form) for form in forms]
unique = [len(set(list(form))) for form in forms_anyone]

print(sum(unique))

# part 2

forms = [form.split() for form in forms]


def find_intersection(answers):
    return functools.reduce(set.intersection, [set(answer) for answer in answers])


forms_everyone = [find_intersection(form) for form in forms]
common = [len(answer_set) for answer_set in forms_everyone]

print(sum(common))