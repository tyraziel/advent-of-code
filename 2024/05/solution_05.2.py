##################################################################################################
# Advent of Code 2024 - Day 5 - Part 2
##################################################################################################

import math

total_of_the_pages = 0

the_rules = []
the_prints = []
good_prints = []
bad_prints = []

#with open('sample_5.txt', 'r') as input_file:
with open('input_5.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    if "|" in the_line:
      the_rules.append(the_line.split("|"))
    if "," in the_line:
      the_prints.append(the_line.split(","))

for the_print in the_prints:
  is_print_valid = True
  for the_rule in the_rules:
    try:
      if the_print.index(the_rule[0]) > the_print.index(the_rule[1]):
        is_print_valid = False
    except:
      a = True
  if is_print_valid:
    good_prints.append(the_print)
  else:
    bad_prints.append(the_print)

for the_bad_print in bad_prints:
  is_print_valid = False
  while not is_print_valid:
    is_print_valid = True
    for the_rule in the_rules:
      try:
        if the_bad_print.index(the_rule[0]) > the_bad_print.index(the_rule[1]):
          is_print_valid = False
          
          the_bad_print[the_bad_print.index(the_rule[0])], the_bad_print[the_bad_print.index(the_rule[1])] = the_bad_print[the_bad_print.index(the_rule[1])], the_bad_print[the_bad_print.index(the_rule[0])]
      except:
        a = True
for bad_print in bad_prints:
  page_to_get = math.floor(len(bad_print) / 2)

  #print(f"Size of Array: {len(bad_print)} -- Going after Element {page_to_get} -- {bad_print}")

  total_of_the_pages = total_of_the_pages + int(bad_print[page_to_get])

print(f"{total_of_the_pages}")