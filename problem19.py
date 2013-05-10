def is_leap_year(year):
  if year % 400 != 0 and year % 100 == 0:
    return False
  if year % 4 == 0:
    return True
  return False

def is_small_month(month):
  return month == 9 or month == 4 or month == 6 or month == 11

def count_days(year, month):
  if month == 2:
    if is_leap_year(year):
      return 29
    else:
      return 28
  elif is_small_month(month):
    return 30
  else:
    return 31
zero_year_days_count = 0

if is_leap_year(1900):
  zero_year_days_count = 366
else:
  zero_year_days_count = 365

start_day = zero_year_days_count % 7

result = 0
day = start_day
for year in range(1901, 2001):
  for month in range(1, 13):
    days_count = count_days(year, month)
    day = (day + days_count) % 7
    if day == 6:
      result += 1

print(result)
