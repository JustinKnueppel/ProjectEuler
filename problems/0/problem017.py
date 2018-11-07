# https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
import re
ones = {0:' ', 1:'one ', 2:'two ', 3:'three ', 4:'four ', 5:'five ', 6:'six ', 7:'seven ', 8:'eight ', 9:'nine '}
tens = {0:' ', 1:' ', 2:'twenty-', 3:'thirty-', 4:'forty-', 5:'fifty-', 6:'sixty-', 7:'seventy-', 8:'eighty-', 9:'ninety-'}
teens = {0:'ten ', 1:'eleven ', 2:'twelve ', 3:'thirteen ', 4:'fourteen ', 5:'fifteen ', 6:'sixteen ', 7:'seventeen ', 8:'eighteen ', 9:'nineteen '}

def getword(number):
    numlist = numtolist(number)
    position = len(numlist)
    word = []
    for i in numlist:
        if position is 2:
            if len(numlist) > 2 and not (i is 0 and numlist[-1] is 0):
                word.append('and ')
            if i is 0:
                position -= 1
                continue
            if i is 1:
                word.append(teens[numlist[-1]])
                return word
            word.append(tens[i])
        else:
            if i is 0:
                position -= 1
                continue
            word.append(ones[i])
            if position is 3:
                word.append('hundred ')
            if position is 4:
                word.append('thousand ')
        position -= 1
    return word

def numtolist(number):
    ls = []
    for i in range(len(str(number))):
        ls.insert(0, number % 10)
        number //= 10
    return ls

def countchars(word):
    regex = re.compile('(\w)')
    matches = regex.findall(word)
    print(''.join(matches))
    return len(matches)

sum = 0
for i in range(1, 1001):
    doot = ''.join(getword(i))
    nurms = countchars(doot)
    sum += nurms
    print(nurms)
print(sum)
