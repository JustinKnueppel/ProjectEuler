# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_leap_year(year):
    """Check if a year is a leap year"""
    if year % 400 is 0:
        return True
    if year % 4 is 0 and year % 100 is not 0:
        return True
    return False

MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
START_YEAR = 1901
def get_num_days(startYear, endYear):
    """returns the number of days in a given range of years"""
    num_days = 0
    for year in range(startYear, endYear):
        for month in range(len(MONTHS)):
            num_days += MONTHS[month]
        if  is_leap_year(year):
            num_days += 1
    return num_days
 

print(get_num_days(1900, 1901))