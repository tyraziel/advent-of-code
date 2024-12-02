##################################################################################################
# Advent of Code 2024 - Day 1 - Solution Part 2
##################################################################################################

list_a = []
list_b = []

with open('input_1.txt', 'r') as input_file:
  for input_line in input_file:
    the_data = input_line.strip().split()
    list_a.append(the_data[0])
    list_b.append(the_data[1])
list_a.sort()
list_b.sort()

the_count = 0

for i in range(len(list_a)):
  the_occurances = 0
  for j in range(len(list_b)):
    if int(list_a[i]) == int(list_b[j]):
      the_occurances = the_occurances + 1
  the_count = the_count + (int(list_a[i]) * the_occurances)

print(f'{the_count}')