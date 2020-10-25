########################################################################
# You are given the following information, but you may prefer 
# to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
#
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not 
# on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the 
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
########################################################################

# https://docs.python.org/3/library/datetime.html
import datetime as dt
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html
import pandas as pd

# 1 Jan 1901 
start = dt.date(1901, 1, 1)
# 31 Dec 2000
end = dt.date(2000, 12, 31)

# Define the range of dates to consider
search_space = pd.date_range(start, end)

# Boolean array determining first days of the month
first_of_months = search_space.map(lambda x: x.day == 1)

# Return the day of the week as an integer, where Monday is 0 and Sunday is 6
sundays = search_space.map(lambda x: x.weekday == 6)

# Boolean multiplication of np arrays to determine the number of first days of the month that are Sundays
calc = sum(first_of_months.values * sundays.values)

print(calc)