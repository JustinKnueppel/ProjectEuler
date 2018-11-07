"""Solution to problem 478 on project euler"""
# https://projecteuler.net/problem=478

# Let us consider mixtures of three substances: A, B and C. A mixture can be described by a ratio of the amounts of A, B, and C in it, i.e., (a : b : c). For example, a mixture described by the ratio (2 : 3 : 5) contains 20% A, 30% B and 50% C.
# For the purposes of this problem, we cannot separate the individual components from a mixture. However, we can combine different amounts of different mixtures to form mixtures with new ratios.
# For example, say we have three mixtures with ratios (3 : 0 : 2), (3 : 6 : 11) and (3 : 3 : 4). By mixing 10 units of the first, 20 units of the second and 30 units of the third, we get a new mixture with ratio (6 : 5 : 9), since:
(10·3/5 + 20·3/20 + 30·3/10 : 10·0/5 + 20·6/20 + 30·3/10 : 10·2/5 + 20·11/20 + 30·4/10)
= (18 : 15 : 27) = (6 : 5 : 9)
# However, with the same three mixtures, it is impossible to form the ratio (3 : 2 : 1), since the amount of B is always less than the amount of C.


# Initial issue loading problem, likely graphic on site