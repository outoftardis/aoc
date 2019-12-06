# day 1
import math
import os

def get_fuel(mass):
    return math.floor(mass / 3) - 2

def fuel_for_fuel(mass):
    fuel = mass
    res_fuel = 0
    while fuel > 0:
        fuel = max(get_fuel(fuel), 0)
        res_fuel += fuel
    return res_fuel

def calculate_fuel(file):
    with open(file, 'r') as f:
        masses = f.read()

    masses = [int(i) for i in masses.split('\n')]    

    # calculating fuel for each mass
    fuel = [get_fuel(mass) for mass in masses]

    # calculating fuel for each mass, and then fuel for fuel, and so on...
    total_fuel = [fuel_for_fuel(mass) for mass in masses]

    return sum(fuel), sum(total_fuel)

script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//001.txt', script_path)

print(calculate_fuel(input_file))
