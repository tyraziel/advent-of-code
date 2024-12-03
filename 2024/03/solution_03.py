##################################################################################################
# Advent of Code 2024 - Day 3
##################################################################################################

import re

mul_total = 0

with open('input_3.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()

    mul_matches = re.findall(r'mul\(\d+,\d+\)', the_line)

    for the_match in mul_matches:
        the_numbers = re.findall(r'\d+', the_match)
        mul_total = mul_total + (int(the_numbers[0]) * int(the_numbers[1]))

print(f'{mul_total}')