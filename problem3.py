#https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math
def listprimes(num):
    primes = []
    for posnum in range(3, int(math.sqrt(num)), 2):
        print('checking', posnum)
        if num % posnum == 0:
            add = True
            for prime in primes:
                if posnum % prime == 0:
                    add = False
            if add:
                primes.append(posnum)
    return primes

print(listprimes(600851475143)[-1])

