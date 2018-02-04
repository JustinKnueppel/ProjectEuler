"""Solution to problem 21 on project euler"""
# https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def get_factors(num):
    """Given a number, return all factors in a list - not 1 or sqrt"""
    factors = [1]
    for i in range(2, int(num ** .5)):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return factors

def is_amicable(num):
    """returns true if the number is an amicable number"""
    first_sum = sum(get_factors(num))
    if num == sum(get_factors(first_sum)) and num != first_sum:
        return True
    return False

amicable_numbers = []
for i in range(2, 10000):
    if is_amicable(i) and i not in amicable_numbers:
        amicable_numbers.append(i)
print(sum(amicable_numbers))
print(is_amicable(220))
print(is_amicable(284))
print(get_factors(220), sum(get_factors(220)))
print(get_factors(284), sum(get_factors(284)))