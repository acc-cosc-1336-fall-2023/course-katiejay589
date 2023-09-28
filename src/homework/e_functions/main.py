# get epoch time for input 3800 seconds

import value_return

result_1 = value_return.get_hour(3800)

result_2 = value_return.get_minutes(3800)

result_3 = value_return.get_seconds(3800)

stuff_in_string = f"time is {result_1:02d}:{result_2:02d}:{result_3:02d}"

print(stuff_in_string)