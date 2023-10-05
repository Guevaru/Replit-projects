def add_time(start, duration, day=None):
  # Extract the start time and period (AM/PM)
  start_time, period = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))

  # Extract the duration time
  duration_hour, duration_minute = map(int, duration.split(':'))

  # Calculate the total minutes
  total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

  # Calculate the new hour and minute
  new_hour = total_minutes // 60 % 12
  new_minute = total_minutes % 60

  # Determine the new period (AM/PM)
  new_period = period
  if total_minutes // 720 % 2 == 1:
    new_period = 'PM' if period == 'AM' else 'AM'

  # Determine the number of days later
  days_later = total_minutes // 1440

  # Determine the day of the week (if provided)
  if day:
    day = day.lower().capitalize()
    days_of_week = [
      'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
      'Saturday'
    ]
    start_day_index = days_of_week.index(day)
    new_day_index = (start_day_index + days_later) % 7
    new_day = days_of_week[new_day_index]
    new_time = f"{new_hour}:{new_minute:02d} {new_period}, {new_day}"
  else:
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

  # Add days later to the output if applicable
  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += f" ({days_later} days later)"

  return new_time
