from math import ceil
def gettrianglenum():
    sum = 0
    counter = 1
    while True:
        sum += counter
        yield sum
        counter += 1

def getfactors(num):
    factors = set()
    for i in range(1, int(ceil(num**.5)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors

def getnumwithfactors(target):
    for tnum in gettrianglenum():
        if len(getfactors(tnum)) > target:
            return tnum

num = getnumwithfactors(500)
print(num)
