"""Solution to problem 477 on project euler"""
# https://projecteuler.net/problem=477

# The number sequence game starts with a sequence S of N numbers written on a line.
# Two players alternate turns. At his turn, a player must select and remove either the first or the last number remaining in the sequence.
# The player score is the sum of all the numbers he has taken. Each player attempts to maximize his own sum.
# Player 1 score is 1 + 10 = 11.
# Let F(N) be the score of player 1 if both players follow the optimal strategy for the sequence S = {s1, s2, ..., sN} defined as:
# The sequence begins with S = {0, 45, 2070, 4284945, 753524550, 478107844, 894218625, ...}.
# You are given F(2) = 45, F(4) = 4284990, F(100) = 26365463243, F(104) = 2495838522951.
# Find F(108).
