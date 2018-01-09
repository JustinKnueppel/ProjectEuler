# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# use binary tree and count the tips
def gettrinum(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

for i in range(1, 5 + 1):
    print(gettrinum(i))
