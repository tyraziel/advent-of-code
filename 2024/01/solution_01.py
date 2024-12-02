##################################################################################################
# Advent of Code 2024 - Day 1 - Solution
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
  the_count = the_count + abs(int(list_a[i]) - int(list_b[i]))

print(f'{the_count}')