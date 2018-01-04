
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
