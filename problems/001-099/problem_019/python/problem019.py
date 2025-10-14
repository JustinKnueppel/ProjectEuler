"""Solution to problem 19 on project euler"""
# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4,
#     but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_leap_year(year):
    """Check if a year is a leap year"""
    if year % 400 is 0:
        return True
    if year % 4 is 0 and year % 100 is not 0:
        return True
    return False

DAYS_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
START_YEAR = 1901
DAY_COUNTER = 2 # Jan 1, 1901 was a Tuesday
def get_num_days_year(year):
    """returns the number of days in a given year"""
    num_days = 0
    for i in range(12):
        num_days += get_num_days_month(i, year)
    return num_days

def get_num_days_month(month, year):
    """Given a month and year, return the number of days in that month"""
    if month is 1 and is_leap_year(year):
        return MONTHS[1] + 1
    return MONTHS[month]

def get_days_until(year, start_year=START_YEAR):
    """Given a final year(exclusive), return the number of days since the starting year"""
    count = 0
    for cur_year in range(start_year, year):
        count += get_num_days_year(cur_year)
    return count

def get_day_of_week(month, year):
    """"Given a month and year, return the day of the week of the first of the given month"""
    day_counter = DAY_COUNTER
    day_counter += get_days_until(year)
    for i in range(month):
        day_counter += get_num_days_month(i, year)
    return DAYS_OF_WEEK[day_counter % 7]

counter = 0
for cur_year in range(1901, 2001):
    print(cur_year)
    for cur_month in range(12):
        if get_day_of_week(cur_month, cur_year) == DAYS_OF_WEEK[0]:
            counter += 1
        print(get_day_of_week(cur_month, cur_year))
print(counter)
