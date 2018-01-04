# https://projecteuler.net/problem=9


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def getpythags(squares):
    triples = []
    for c in squares[::-1]:
        for b in squares:
            if c - b in squares:
                triples.append((int((c-b)**.5), int((b)**.5), int((c)**.5)))
    return triples

def matchestarget(triple):
    TARGET_SUM = 1000 #5, 12, 13
    n1, n2, n3 = triple
    return n1 + n2 + n3 == TARGET_SUM

squares = [i**2 for i in range(1, 1000)]
triples = getpythags(squares)
for triple in triples:
    if matchestarget(triple):
        print(triple)
