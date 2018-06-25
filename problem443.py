"""Solution to problem 443 on project euler"""
# https://projecteuler.net/problem=443

# Let g(n) be a sequence defined as follows:
g(4) = 13,
g(n) = g(n-1) + gcd(n, g(n-1)) for n > 4.
# The first few values are:
# You are given that g(1 000) = 2524 and g(1 000 000) = 2624152.
# Find g(1015).
