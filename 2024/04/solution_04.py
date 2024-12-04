##################################################################################################
# Advent of Code 2024 - Day 4
##################################################################################################

import re

total_XMAS = 0

the_matrix = [] #has you!

#Convert the input into a 2D array (or Matrix if you must)
with open('input_4.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    the_matrix.append(list(the_line))

for i in range(len(the_matrix)):  # i is row (NORTH/SOUTH)
  for j in range(len(the_matrix[i])):  #j is col (WEST/EAST)

    #Check if the character we're at is an X if so, we need to check all 8 directions (with bounding)
    if the_matrix[i][j] == 'X':

      #Go EAST
      if j + 3 < len(the_matrix[i]) and the_matrix[i][j+1] == 'M' and the_matrix[i][j+2] == 'A' and the_matrix[i][j+3] == 'S':
        total_XMAS = total_XMAS + 1
      #Go SOUTH
      if i + 3 < len(the_matrix) and the_matrix[i+1][j] == 'M' and the_matrix[i+2][j] == 'A' and the_matrix[i+3][j] == 'S':
        total_XMAS = total_XMAS + 1
      #Go WEST
      if j - 3 >= 0 and the_matrix[i][j-1] == 'M' and the_matrix[i][j-2] == 'A' and the_matrix[i][j-3] == 'S':
        total_XMAS = total_XMAS + 1
      #Go NORTH
      if i - 3 >= 0 and the_matrix[i-1][j] == 'M' and the_matrix[i-2][j] == 'A' and the_matrix[i-3][j] == 'S':
        total_XMAS = total_XMAS + 1

      #Go SOUTH/EAST
      if j + 3 < len(the_matrix[i]) and i + 3 < len(the_matrix) and the_matrix[i+1][j+1] == 'M' and the_matrix[i+2][j+2] == 'A' and the_matrix[i+3][j+3] == 'S':
        total_XMAS = total_XMAS + 1
      #Go SOUTH/WEST
      if j - 3 >= 0 and i + 3 < len(the_matrix) and the_matrix[i+1][j-1] == 'M' and the_matrix[i+2][j-2] == 'A' and the_matrix[i+3][j-3] == 'S':
        total_XMAS = total_XMAS + 1
      #Go NORTH/EAST
      if j + 3 < len(the_matrix[i]) and i - 3 >= 0 and the_matrix[i-1][j+1] == 'M' and the_matrix[i-2][j+2] == 'A' and the_matrix[i-3][j+3] == 'S':
        total_XMAS = total_XMAS + 1
      #Go NORTH/WEST
      if j - 3 >= 0 and i - 3 >= 0 and the_matrix[i-1][j-1] == 'M' and the_matrix[i-2][j-2] == 'A' and the_matrix[i-3][j-3] == 'S':
        total_XMAS = total_XMAS + 1

print(f'{total_XMAS}')