##################################################################################################
# Advent of Code 2024 - Day 7 - Part 2
##################################################################################################

#Borrowed from here - https://stackoverflow.com/questions/33792694/base-convert-in-python-given-a-string/33802414#33802414
def to_base(n, bse):
    digs = "0123456789abcdefghijklmnopqrstuvwxyz"
    tmp = []
    while n:
        n, i = divmod(n, bse)
        tmp.append(digs[i])
    return "".join(tmp[::-1])

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

  #print(f"Number of operators: {the_number_of_operators} - {3**the_number_of_operators}")
  for i in range(3**the_number_of_operators):  #i is the operators representation in ternary -- 0 -> + -- 1 -> * -- 2 -> ||
    the_current_answer = int(the_operands[0])
    the_operand_index = 1
    the_operators = to_base(i,3).zfill(the_number_of_operators)
    #print(f"{the_operators}")
    for operator in list(the_operators):
      if operator == "0":
        the_current_answer = the_current_answer + int(the_operands[the_operand_index])
      elif operator == "1":
        the_current_answer = the_current_answer * int(the_operands[the_operand_index])
      elif operator == "2":
        the_current_answer = int(f"{str(the_current_answer)}{the_operands[the_operand_index]}")
      else:
        print("ERROR")
      the_operand_index = the_operand_index + 1
    if the_current_answer == the_answer:
      solvable = True
      break

  if solvable:
    sum_of_all = sum_of_all + the_answer

print(f"{sum_of_all}")