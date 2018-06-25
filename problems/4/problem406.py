"""Solution to problem 406 on project euler"""
# https://projecteuler.net/problem=406

# We are trying to find a hidden number selected from the set of integers {1, 2, ..., n} by asking questions. 
Each number (question) we ask, we get one of three possible answers:
# Given the value of n, a, and b, an optimal strategy minimizes the total cost for the worst possible case.
# For example, if n = 5, a = 2, and b = 3, then we may begin by asking "2" as our first question.
# If we are told that 2 is higher than the hidden number (for a cost of b=3), then we are sure that "1" is the hidden number (for a total cost of 3).
If we are told that 2 is lower than the hidden number (for a cost of a=2), then our next question will be "4".
If we are told that 4 is higher than the hidden number (for a cost of b=3), then we are sure that "3" is the hidden number (for a total cost of 2+3=5).
If we are told that 4 is lower than the hidden number (for a cost of a=2), then we are sure that "5" is the hidden number (for a total cost of 2+2=4).
Thus, the worst-case cost achieved by this strategy is 5. It can also be shown that this is the lowest worst-case cost that can be achieved. 
So, in fact, we have just described an optimal strategy for the given values of n, a, and b.
# Let C(n, a, b) be the worst-case cost achieved by an optimal strategy for the given values of n, a, and b.


# Initial issue loading problem, likely graphic on site