#https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def getprime(primes):
    yield 2
    curnum = 3
    while True:
        add = True
        for prime in primes: #only go up to n^.5
            if curnum**.5 < prime:
                break
            if curnum % prime == 0:
                add = False
                break
        if add:
            yield curnum
        curnum += 2

primes = []
for curnum in getprime(primes):
    if curnum >= 2000000:
        break
    print(curnum)
    primes.append(curnum)
print(primes[0])
print(primes[-1])
print(sum(primes))

