"""Solution to problem 230 on project euler"""
# https://projecteuler.net/problem=230

# For any two strings of digits, A and B, we define FA,B to be the sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the previous two.
# Further, we define DA,B(n) to be the nth digit in the first term of FA,B that contains at least n digits.
# Example:
# Let A=1415926535, B=8979323846. We wish to find DA,B(35), say.
# The first few terms of FA,B are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846
# Then DA,B(35) is the 35th digit in the fifth term, which is 9.


# Initial issue loading problem, likely graphic on site