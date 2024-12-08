##################################################################################################
# Advent of Code 2024 - Day 7
##################################################################################################
the_problems = []
solvable_problems = []

sum_of_all = 0

with open('input_7.txt', 'r') as input_file:
  for input_line in input_file:
    the_line = input_line.strip()
    the_problems.append(the_line.split(" "))
    the_problems[-1][0] = the_problems[-1][0][:-1]

for the_problem in the_problems:
  solvable = False
  the_answer = int(the_problem[0])
  the_operands = the_problem[1:]
  the_number_of_operators = len(the_operands) - 1

  #print(f"Number of operators: {the_number_of_operators} - {2**the_number_of_operators}")
  for i in range(2**the_number_of_operators):  #i is the operators representation in binary -- 0 -> + -- 1 -> *
    #print(f"{bin(i)[2:].zfill(the_number_of_operators)}")
    the_current_answer = int(the_operands[0])
    the_operand_index = 1
    the_operators = bin(i)[2:].zfill(the_number_of_operators) #https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python/10411184#10411184
    for operator in list(the_operators):
      if operator == "0":
        the_current_answer = the_current_answer + int(the_operands[the_operand_index])
      elif operator == "1":
        the_current_answer = the_current_answer * int(the_operands[the_operand_index])
      else:
        print("ERROR")
      the_operand_index = the_operand_index + 1
    if the_current_answer == the_answer:
      solvable = True
      break

  if solvable:
    sum_of_all = sum_of_all + the_answer

print(f"{sum_of_all}")