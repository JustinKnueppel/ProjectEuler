#https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#recursive solution
MAX_NUM = 4000000
sum = 0

def fib(n):
    assert n >= 0, "num must be greater than 0"
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

reps = 1
num = fib(reps)
while num <= MAX_NUM:
    if num % 2 == 0:
        sum += num
    reps += 1
    num = fib(reps)

print(sum)

#faster solution is to build a list bottom up starting with [0, 1] and just add the previous two nums to append to the list