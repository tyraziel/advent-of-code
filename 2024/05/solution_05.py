##################################################################################################
# Advent of Code 2024 - Day 5
##################################################################################################

import math

total_of_the_pages = 0

the_rules = []
the_prints = []
good_prints = []

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
  #the_pages = the_print.split(",")
  for the_rule in the_rules:
    try:
      if the_print.index(the_rule[0]) > the_print.index(the_rule[1]):
        is_print_valid = False
    except:
      a = True
  if is_print_valid:
    good_prints.append(the_print)

for good_print in good_prints:
  page_to_get = math.floor(len(good_print) / 2)

  #print(f"Size of Array: {len(good_print)} -- Going after Element {page_to_get} -- {good_print}")

  total_of_the_pages = total_of_the_pages + int(good_print[page_to_get])


#print(f"{len(good_prints)} vs {len(the_prints)}")
print(f"{total_of_the_pages}")