# day 8

import os
import numpy
import re

m = 25
n = 6
k = m * n

def check(layers):

    zero_count = [layer.count('0') for layer in layers]
    few_zero = numpy.argmin(zero_count)
    ones = layers[few_zero].count('1')
    twos = layers[few_zero].count('2')

    return ones * twos

def get_color(s):
    # s - string of color codes from all the layers -- corresponding to a particular pixel
    # find the first non-transparent element of the string

    for c in s:
        if c != '2':
            return c
    return '2'

def get_pixel_colors(image):
    pixel_columns = [image[i::k] for i in range(0, k)]
    image_colors = ''.join([get_color(column) for column in pixel_columns])

    return image_colors

def print_image(image):
    colored_image = get_pixel_colors(image)
    rows = [colored_image[i:i+m] for i in range(0, len(colored_image), m)]
    rows = [re.sub('0', ' ', row) for row in rows]
    for row in rows:
        print(row)


script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//008.txt', script_path)

with open(input_file, 'r') as f:
    image = f.read()

layers = [image[i:i+k] for i in range(0, len(image), k)]

# task 1
print(check(layers))

# task 2
print_image(image)

