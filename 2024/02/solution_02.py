##################################################################################################
# Advent of Code 2024 - Day 2 - Solution
##################################################################################################

safe_report_count = 0
unsafe_report_count = 0

with open('input_2.txt', 'r') as input_file:
  for input_line in input_file:
    report_is_safe = True
    direction_evaluated = False
    report_increasing = False
    report_decreasing = False
    the_data = input_line.strip().split()
    previous_data = int(the_data[0])
    # print(f'{the_data}')

    for value in the_data[1:]:
      value = int(value)

      if not direction_evaluated and value > previous_data:
        report_increasing = True
        direction_evaluated = True
      elif not direction_evaluated and value < previous_data:
        report_decreasing = True
        direction_evaluated = True
      elif not report_increasing and value > previous_data:
        report_is_safe = False
        # print(f'Report is NOT Safe - report started increasing but changed')
      elif not report_decreasing and value < previous_data:
        report_is_safe = False
        # print(f'Report is NOT Safe - report started decreasing but changed')

      # print(f'Comparing {previous_data} with {value} for result of {abs(previous_data - value)}')
      if abs(previous_data - value) == 0 or abs(previous_data - value) > 3:
        report_is_safe = False
        # print(f'Report is NOT Safe')
      previous_data = value

    if report_is_safe:
      # print(f'Report is Safe')
      safe_report_count = safe_report_count + 1
    else:
      unsafe_report_count = unsafe_report_count + 1

print(f'{safe_report_count}')
# print(f'Safe:  {safe_report_count}')
# print(f'Unsafe:  {unsafe_report_count}')