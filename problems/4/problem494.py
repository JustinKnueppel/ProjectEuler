"""Solution to problem 494 on project euler"""
# https://projecteuler.net/problem=494

# 
The Collatz sequence is defined as:
$a_{i+1} = \left\{  \large{\frac {a_i} 2 \atop 3 a_i+1} {\text{if }a_i\text{ is even} \atop \text{if }a_i\text{ is odd}} \right.$.

# 
The Collatz conjecture states that starting from any positive integer, the sequence eventually reaches the cycle 1,4,2,1....
We shall define the sequence prefix p(n) for the Collatz sequence starting with a1 = n as the sub-sequence of all numbers not a power of 2 (20=1 is considered a power of 2 for this problem). For example:p(13) = {13, 40, 20, 10, 5} p(8) = {}
Any number invalidating the conjecture would have an infinite length sequence prefix.



# Initial issue loading problem, likely graphic on site