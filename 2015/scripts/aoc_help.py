import os


def get_input(day):
    script_path = os.path.dirname(__file__)
    input_file = os.path.relpath('..//input//{}.txt'.format(day), script_path)

    with open(input_file, 'r') as f:
        day_input = f.read()

    return day_input
