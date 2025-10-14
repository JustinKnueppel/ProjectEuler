# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def countup(num):
    #counts up from 1-infinity
    i = num
    while True:
        i += 1
        yield i

def getprime(primes, num):
    curnum = -1
    for i in countup(num):
        add = True
        for prime in primes:
            if i % prime == 0:
                add = False
                break
        if add:
            curnum = i
            break
    return curnum

counter = 1
curnum = 1
primes = []#2, 3, 5, 7]
while counter <= 10001:
    curnum = getprime(primes, curnum)
    print(curnum)
    primes.append(curnum)
    counter += 1
print(primes[-1])
