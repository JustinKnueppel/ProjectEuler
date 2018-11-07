"""Solution to problem 545 on project euler"""
# https://projecteuler.net/problem=545

# The sum of the kth powers of the first n positive integers can be expressed as a polynomial of degree k+1 with rational coefficients, the Faulhaber's Formulas:
$1^k + 2^k + ... + n^k = \sum_{i=1}^n i^k = \sum_{i=1}^{k+1} a_{i} n^i = a_{1} n + a_{2} n^2 + ... + a_{k} n^k + a_{k+1} n^{k + 1}$,
where ai's are rational coefficients that can be written as reduced fractions pi/qi (if ai = 0, we shall consider qi = 1).
# For example, $1^4 + 2^4 + ... + n^4 = -\frac 1 {30} n + \frac 1 3 n^3 + \frac 1 2 n^4 + \frac 1 5 n^5.$


# Initial issue loading problem, likely graphic on site