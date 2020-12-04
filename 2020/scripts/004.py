import aoc_help as aoc
import re


def split_passport(passport):
    passport = {field.split(":")[0]: field.split(":")[1] for field in passport}
    return passport


def check_valid(passport):
    n = len(passport)
    valid = n == 8 or (n == 7 and "cid" not in passport.keys())
    return valid


def check_year(passport, type, start, finish):
    return start <= int(passport[type]) <= finish


def check_height(height_field):
    if bool(re.match("\d{2,3}(cm|in)", height_field)):
        height = int(height_field[:-2])
        unit = height_field[-2:]
        return (unit == "cm" and 150 <= height <= 193) or (unit == "in" and 59 <= height <= 76)
    return False


def check_more(passport):
    valid = False
    if check_valid(passport):
        valid = check_year(passport, "byr", 1920, 2002) and \
                check_year(passport, "iyr", 2010, 2020) and \
                check_year(passport, "eyr", 2020, 2030) and \
                check_height(passport["hgt"]) and \
                bool(re.fullmatch("#[a-f\d]{6}", passport["hcl"])) and \
                bool(re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", passport["ecl"])) and \
                bool(re.fullmatch("\d{9}", passport["pid"]))
    return valid


data = aoc.get_input('004')
data = data.split('\n\n')
data = [re.split("\n|\s", passport) for passport in data]
data = [split_passport(passport) for passport in data]

# part 1

validness = [check_valid(passport) for passport in data]
print(sum(validness))

# part 2

validness_full = [check_more(passport) for passport in data]
print(sum(validness_full))