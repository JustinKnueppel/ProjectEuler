#https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
MIN_VAL = 0
MAX_VAL = 1000
MULTIPLES = (3, 5)
usedNums = set()
sum = 0

for number in MULTIPLES:
    CUR_NUM = number
    while CUR_NUM < MAX_VAL:
        if not CUR_NUM in usedNums:
            sum += CUR_NUM
            usedNums.add(CUR_NUM)
        CUR_NUM += number

print(sum)




