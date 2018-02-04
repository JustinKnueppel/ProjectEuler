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
        if num % i is 0:
            factors.append(i)
            factors.append(num // i)
    return factors

print(sum(get_factors(220)))