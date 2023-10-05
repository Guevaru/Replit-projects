# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time

# Test case 1
start_time = "3:00 PM"
duration = "3:10"
result = add_time(start_time, duration)
print(result)

# Test case 2
start_time = "11:30 AM"
duration = "2:32"
day = "Monday"
result = add_time(start_time, duration, day)
print(result)

# Test case 3
start_time = "11:43 AM"
duration = "00:20"
result = add_time(start_time, duration)
print(result)

# Test case 4
start_time = "10:10 PM"
duration = "3:30"
result = add_time(start_time, duration)
print(result)

# Test case 5
start_time = "11:43 PM"
duration = "24:20"
day = "tueSday"
result = add_time(start_time, duration, day)
print(result)

# Test case 6
start_time = "6:30 PM"
duration = "205:12"
result = add_time(start_time, duration)
print(result)
