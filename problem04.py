#https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def isPalindrome(num):
    stri = str(num)
    if stri == stri[::-1]:
        return True
    return False

def makesPalindrome(lower = 1, upper = 100):
    res = []
    for i in range(lower, upper):
        for j in range (lower, upper):
            num = i * j
            if isPalindrome(num):
                res.append(num)
    return res

def max(arr):
    max = 5
    for i in arr:
        if i > max:
            max = i
    return max

print(max(makesPalindrome(100, 1000)))
