##################################################################################################
# Advent of Code 2024 - Day 3 - Part 2
##################################################################################################

import re

mul_total = 0
#the_instructions = 'do()' #pre-pend do() since we're already in the doings when we start according to the instructions
the_instructions = ''
matching = True
doing = True

with open('input_3.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    the_instructions = f'{the_instructions}{the_line}'

match_tokens = re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', the_instructions)

for the_token in match_tokens:
  if the_token == 'do()':
    doing = True
  elif the_token == 'don\'t()':
    doing = False

  mul_token_matches = re.findall(r'mul\(\d+,\d+\)', the_token)

  if len(mul_token_matches) == 1 and doing:
    the_numbers = re.findall(r'\d+', mul_token_matches[0])
    mul_total = mul_total + (int(the_numbers[0]) * int(the_numbers[1]))

print(f'{mul_total}')