##################################################################################################
# Advent of Code 2024 - Day 4 - Part 2
##################################################################################################

import re

total_XMAS = 0

the_matrix = [] #has you!

#Convert the input into a 2D array (or Matrix if you must)
with open('input_4.txt', 'r') as input_file:
#with open('sample_4.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    the_matrix.append(list(the_line))

for i in range(len(the_matrix)):  # i is row (NORTH/SOUTH)
  for j in range(len(the_matrix[i])):  #j is col (WEST/EAST)

    if the_matrix[i][j] == 'A':
      if j + 1 < len(the_matrix[i]) and i + 1 < len(the_matrix) and the_matrix[i+1][j+1] == 'S':
        if j + 1 < len(the_matrix[i]) and i - 1 >= 0 and the_matrix[i-1][j+1] == 'S':
          if j - 1 >= 0 and i + 1 < len(the_matrix) and the_matrix[i+1][j-1] == 'M':
            if j - 1 >= 0 and i - 1 >= 0 and the_matrix[i-1][j-1] == 'M':
              total_XMAS = total_XMAS + 1

    if the_matrix[i][j] == 'A':
      if j + 1 < len(the_matrix[i]) and i + 1 < len(the_matrix) and the_matrix[i+1][j+1] == 'M':
        if j + 1 < len(the_matrix[i]) and i - 1 >= 0 and the_matrix[i-1][j+1] == 'M':
          if j - 1 >= 0 and i + 1 < len(the_matrix) and the_matrix[i+1][j-1] == 'S':
            if j - 1 >= 0 and i - 1 >= 0 and the_matrix[i-1][j-1] == 'S':
              total_XMAS = total_XMAS + 1

    if the_matrix[i][j] == 'A':
      if j + 1 < len(the_matrix[i]) and i + 1 < len(the_matrix) and the_matrix[i+1][j+1] == 'M':
        if j + 1 < len(the_matrix[i]) and i - 1 >= 0 and the_matrix[i-1][j+1] == 'S':
          if j - 1 >= 0 and i + 1 < len(the_matrix) and the_matrix[i+1][j-1] == 'M':
            if j - 1 >= 0 and i - 1 >= 0 and the_matrix[i-1][j-1] == 'S':
              total_XMAS = total_XMAS + 1

    if the_matrix[i][j] == 'A':
      if j + 1 < len(the_matrix[i]) and i + 1 < len(the_matrix) and the_matrix[i+1][j+1] == 'S':
        if j + 1 < len(the_matrix[i]) and i - 1 >= 0 and the_matrix[i-1][j+1] == 'M':
          if j - 1 >= 0 and i + 1 < len(the_matrix) and the_matrix[i+1][j-1] == 'S':
            if j - 1 >= 0 and i - 1 >= 0 and the_matrix[i-1][j-1] == 'M':
              total_XMAS = total_XMAS + 1

print(f'{total_XMAS}')