#https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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

curnum = 1
sum = 0
primes = []#2, 3, 5, 7]
while curnum <= 2000000:
    curnum = getprime(primes, curnum)
    print(curnum)
    sum += curnum
    primes.append(curnum)
print(primes[0])
print(sum)

#first prime - 2
#last prime - 2000003
# sum with last prime - 142915828925
# sum without last prime (answer) = 142913828922
