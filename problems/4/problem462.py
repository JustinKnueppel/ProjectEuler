"""Solution to problem 462 on project euler"""
# https://projecteuler.net/problem=462

# 
A 3-smooth number is an integer which has no prime factor larger than 3. For an integer N, we define S(N) as the set of 3-smooth numbers less than or equal to N . For example, S(20) = { 1, 2, 3, 4, 6, 8, 9, 12, 16, 18 }.

# 
We define F(N) as the number of permutations of S(N) in which each element comes after all of its proper divisors.

# 
This is one of the possible permutations for N = 20.
- 1, 2, 4, 3, 9, 8, 16, 6, 18, 12.
This is not a valid permutation because 12 comes before its divisor 6.
- 1, 2, 4, 3, 9, 8, 12, 16, 6, 18.



# Initial issue loading problem, likely graphic on site