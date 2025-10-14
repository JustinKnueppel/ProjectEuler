# https://projecteuler.net/problem=16



# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
import math
power = 1000
num = int(math.pow(2,power))
print(num)
sum = 0
for i in str(num):
    sum += int(i)
print(sum)
