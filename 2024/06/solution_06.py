##################################################################################################
# Advent of Code 2024 - Day 6
##################################################################################################

the_matrix = [] #has you!
the_guard_i = -1
the_guard_j = -1
the_guard_delta_i = -1
the_guard_delta_j = 0

the_unique_places_visited = 0

#Convert the input into a 2D array (or Matrix if you must)
with open('input_6.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    the_matrix.append(list(the_line))

for i in range(len(the_matrix)):  # i is row (NORTH/SOUTH) 
  for j in range(len(the_matrix[i])):  #j is col (WEST/EAST) 
    if the_matrix[i][j] == '^':
      the_guard_i = i
      the_guard_j = j
      the_matrix[i][j] = 'X'

while the_guard_i > 0 and the_guard_i < len(the_matrix) and the_guard_j > 0 and the_guard_j < len(the_matrix[0]):
  #Check if the spot in front of the guard is open, then go into it
  if the_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j] == '.' or the_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j] == 'X':
    the_guard_i = the_guard_i+the_guard_delta_i
    the_guard_j = the_guard_j+the_guard_delta_j
    the_matrix[the_guard_i][the_guard_j] = 'X'
  elif the_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j] == '#':
    #moviing up so make them move right
    if the_guard_delta_i == -1:
      the_guard_delta_i = 0
      the_guard_delta_j = 1
    #moving right so make them move down
    elif the_guard_delta_j == 1:
      the_guard_delta_i = 1
      the_guard_delta_j = 0
    #moving down so make them move left
    elif the_guard_delta_i == 1:
      the_guard_delta_i = 0
      the_guard_delta_j = -1
    #moving left so make them move up
    elif the_guard_delta_j == -1:
      the_guard_delta_i = -1
      the_guard_delta_j = 0

for i in range(len(the_matrix)):  # i is row (NORTH/SOUTH) 
  for j in range(len(the_matrix[i])):  #j is col (WEST/EAST) 
    if the_matrix[i][j] == 'X':
      the_unique_places_visited = the_unique_places_visited + 1


print(f"{the_unique_places_visited}")