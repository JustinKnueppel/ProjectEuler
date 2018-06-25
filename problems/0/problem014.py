# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Use dictionary to store previous lengths

class Collatz:
    def __init__(self):
        self.storednums = {}

    def getnextnum(self, num):
        return num * 3 + 1 if num % 2 else num // 2

    def getcollatz(self, orignum):
        num = orignum
        nums = []
        while True:
            if num in self.storednums.keys():
                self.storednums[orignum] = len(nums) + self.storednums[num]
                return self.storednums[orignum]
            nums.append(num)
            if num == 1:
                self.storednums[orignum] = len(nums)
                return self.storednums[orignum]
            num = self.getnextnum(num)

obj = Collatz()
maxnum = 1000000
maxlen = (0,0)
for i in range(1, maxnum):
    curnum = obj.getcollatz(i)
    print(i)
    if curnum > maxlen[1]:
        maxlen = (i, curnum)

print(maxlen)
