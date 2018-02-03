"""Solution to problem 20 on project euler"""

#find the total of the digits of 100!

def factorial(num):
    """returns the factorial of the argument (num >= 0)"""
    arr = [1, 1]
    for i in range(2, num + 1):
        arr.append(arr[-1] * i)
    return arr[-1]

def count_digits(num):
    """finds the sum of each digit in an integer"""
    total = 0
    while num is not 0:
        total += num % 10
        num //= 10
    return total

print(count_digits(factorial(100)))
