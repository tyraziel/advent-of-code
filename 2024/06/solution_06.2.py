##################################################################################################
# Advent of Code 2024 - Day 6 - Part 2
##################################################################################################

import copy

the_matrix = [] #has you!
the_guard_starting_i = -1
the_guard_starting_j = -1
the_guard_i = -1
the_guard_j = -1
the_guard_delta_i = -1
the_guard_delta_j = 0

loopable_spots_found = 0

#Convert the input into a 2D array (or Matrix if you must)
with open('input_6.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    the_matrix.append(list(the_line))

iterations = len(the_matrix) * len(the_matrix[0])

#print(f"Iterations {iterations} i-{len(the_matrix)} j-{len(the_matrix[0])}")

for i in range(len(the_matrix)):  # i is row (NORTH/SOUTH) 
  for j in range(len(the_matrix[i])):  #j is col (WEST/EAST) 
    if the_matrix[i][j] == '^':
      the_guard_starting_i = i
      the_guard_starting_j = j
      the_matrix[i][j] = 'X'

iteration_count = 0

for i in range(len(the_matrix)):  # i is row (NORTH/SOUTH) 
  for j in range(len(the_matrix[i])):  #j is col (WEST/EAST)
    iteration_count = iteration_count + 1

    the_temp_matrix = []
    loop_discovered = False
    the_guard_delta_i = -1
    the_guard_delta_j = 0
    the_guard_i = the_guard_starting_i
    the_guard_j = the_guard_starting_j

    #print(f"Checking object at {i}, {j}")
    if the_matrix[i][j] == '.':
      for ii in range(len(the_matrix)):
        the_temp_matrix.append([])
        for jj in range(len(the_matrix[ii])):
          the_temp_matrix[ii].append([])
          the_temp_matrix[ii][jj] = copy.deepcopy([the_matrix[ii][jj], 0, 0])

      #print(f"{len(the_temp_matrix)} {len(the_temp_matrix[0])}")

      #we already know we're good to flip from . to # for our run
      #print(f"Placing object at {i}, {j}")
      the_temp_matrix[i][j] = '#'

      while (the_guard_i > 0 and the_guard_i < len(the_temp_matrix) and the_guard_j > 0 and the_guard_j < len(the_temp_matrix[0])) and not loop_discovered:
        #Check if the spot in front of the guard is open, then go into it
        try:
          if the_temp_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j][0] == '.' or the_temp_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j][0] == 'X':
            the_guard_i = the_guard_i+the_guard_delta_i
            the_guard_j = the_guard_j+the_guard_delta_j
            #5, 38 is the loop
            #if i == 5 and j == 38:
              #print(f"[{i},{j}] The Guard is Entering at {the_guard_i} {the_guard_j} with direction {the_guard_delta_i} {the_guard_delta_j} and we came in here before with {the_temp_matrix[the_guard_i][the_guard_j][1]} {the_temp_matrix[the_guard_i][the_guard_j][1]}")
            if the_temp_matrix[the_guard_i][the_guard_j][1] == the_guard_delta_i and the_temp_matrix[the_guard_i][the_guard_j][2] == the_guard_delta_j:
              #print("WE FOUND A LOOP")
              loop_discovered = True
            the_temp_matrix[the_guard_i][the_guard_j][0] = 'X'
            the_temp_matrix[the_guard_i][the_guard_j][1] = the_guard_delta_i
            the_temp_matrix[the_guard_i][the_guard_j][2] = the_guard_delta_j
          elif the_temp_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j][0] == '#':
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
          else:
            print(f"ERROR {the_temp_matrix[the_guard_i+the_guard_delta_i][the_guard_j+the_guard_delta_j][0]}")
        except:
          break

    if loop_discovered:
      print('O', end='')
      loopable_spots_found = loopable_spots_found + 1
    else:
      print(f'{the_matrix[i][j]}', end='')
    if iteration_count % len(the_matrix[0]) == 0:
      print(f"{iteration_count/iterations}")

print(f"{loopable_spots_found}")