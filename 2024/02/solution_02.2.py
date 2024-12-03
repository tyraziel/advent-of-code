##################################################################################################
# Advent of Code 2024 - Day 2 - Solution Part 2
##################################################################################################

safe_report_count = 0
unsafe_report_count = 0

with open('input_2.txt', 'r') as input_file:
  for input_line in input_file:
    report_is_safe = False

    for i in range(-1, len(input_line.strip().split())):
      print(f'{i}')
      the_data = input_line.strip().split()
      if i >= 0:
        del the_data[i]

      sub_report_is_safe = True
      direction_evaluated = False
      report_increasing = False
      report_decreasing = False
      
      previous_data = int(the_data[0])

      for value in the_data[1:]:
        value = int(value)

        if not direction_evaluated and value > previous_data:
          report_increasing = True
          direction_evaluated = True
        elif not direction_evaluated and value < previous_data:
          report_decreasing = True
          direction_evaluated = True
        elif not report_increasing and value > previous_data:
          sub_report_is_safe = False
        elif not report_decreasing and value < previous_data:
          sub_report_is_safe = False

        if abs(previous_data - value) == 0 or abs(previous_data - value) > 3:
          sub_report_is_safe = False

        previous_data = value

      if sub_report_is_safe:
        report_is_safe = True

    if report_is_safe:
      safe_report_count = safe_report_count + 1
    else:
      unsafe_report_count = unsafe_report_count + 1

print(f'{safe_report_count}')