# https://projecteuler.net/problem=5


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisByAll(lower = 1, upper = 10):
    res = 1
    for i in range(lower, upper):
        res *= i
    return res

# def canmake(num, arr):
    #take a list of nums and see if they can make the target num by multiplication

def numofeach(num):
    #initializes a numx2 array with each number/2 and their counts
    res = []
    for i in range (1, num // 2 + 1):
        res.append([i, 0])
    return res

print(divisByAll())
print(9 * 8 * 7 * 5 )
arr = numofeach(9)
for i in range(len(arr)):
    print(arr[i])
