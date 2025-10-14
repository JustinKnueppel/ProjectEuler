# https://projecteuler.net/problem=5


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import BinaryTree
def getfinaldict(upper = 10, lower = 2):
    totaldict = {}
    for i in range (lower, upper + 1):
        nod = BinaryTree.Node(i)
        factors = makedict(nod.getlefts(nod.getfactors(nod)))
        totaldict = mergedict(factors, totaldict)
    return totaldict

def gettotal(finaldict):
    total = 1
    for i in finaldict.keys():
        total *= i**finaldict[i]
    return total

def makedict(factors):
    dict = {}
    for i in factors:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def mergedict(factors, totals):
    for i in factors.keys():
        if i in totals.keys():
            if factors[i] > totals[i]:
                totals[i] = factors[i]
        else:
            totals[i] = factors[i]
    return totals

# print(gettotal(getfinaldict(10)))
print(gettotal(getfinaldict()))
print(gettotal(getfinaldict(20)))
print(gettotal(getfinaldict(100)))
