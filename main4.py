import datetime


def gen_secs():
  """
  all the hefreshei seconds between 0-59
  """
  for sec in range(60):
    yield sec


def gen_minutes():
  """
  all the hefreshei minutes between 0-59
  """
  for minute in range(60):
    yield minute


def gen_hours():
  """
    create all the hefreshei hours that possible between 0-23
  """
  for hour in range(24):
    yield hour


def gen_time():
  """
  create all the possible hours per day from 00:00:00
  """
  for sec in gen_secs():
    for minute in gen_minutes():
      for hour in gen_hours():
        yield f"{hour:02d}:{minute:02d}:{sec:02d}"


def gen_years(start=2019):
  """
  get the year from start and while it true
  """
  year = start
  while True:
    yield year
    year += 1


def gen_months():
  """
  create all the months in the year 1-12
  """
  for month in range(1, 13):
    yield month


def gen_days(month, leap_year=True):
  """
  get the number of days in the correct month).
  """
  if month in {4, 6, 9, 11}:
    days = 30
  elif month == 2:
    if leap_year:
      days = 29
    else:
      days = 28
  else:
    days = 31
  for day in range(1, days + 1):
    yield day


def gen_date():
  """
  create a date by this format dd/mm/yyyy .
  """
  for year in gen_years():
    for month in gen_months():
      for day in gen_days(month, leap_year=is_leap_year(year)):
        for hour in gen_hours():
          for minute in gen_minutes():
            for sec in gen_secs():
              yield f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minute:02d}:{sec:02d}"


def is_leap_year(year):
  """
  check if the year is normal or meoberet
  """
  if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False


if __name__ == "__main__":
  # print 10 examples
  for i in range(10):
    print(next(gen_date()))

  # print 1,000,000 itorations
  count = 0
  for date in gen_date():
    print(date)
    count += 1
    if count % 1000000 == 0:
      input("push enter to continue")
