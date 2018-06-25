"""Solution to problem 23 on project euler"""
# https://projecteuler.net/problem=23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the 
# number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be 
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown 
# that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known 
# that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# 4179871

def get_factors(num):
    factors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    return factors

def is_abundant(num):
    if sum(get_factors(num)) > num:
        return True
    return False

def addable(num, abunds):
    for i in abunds:
        if i > num - 11:
            return False
        if num - i in abunds:
            return True
    return False


abundant_nums = [12]
for i in range(13, 28115):
    if is_abundant(i):
        abundant_nums.append(i)
print("done getting abundant nums")
not_addable_nums = []
for i in range(28124):
    print(i)
    if not addable(i, abundant_nums):
        not_addable_nums.append(i)
print(sum(not_addable_nums))