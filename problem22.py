"""Solution to problem 22 on Project Euler"""
# https://projecteuler.net/problem=22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
import re
ALPHA = "abcdefghijklmnopqrstuvwxyz"

name_regex = re.compile(r'''(
(")
(\w+)
(")
)''', re.VERBOSE | re.IGNORECASE)

def score_name(name):
    """returns the lexiographic score of a word"""
    total = 0
    for letter in name:
        total += ALPHA.find(letter) + 1
    return total

def get_names(file_name):
    """Given a file name, return a list of all names"""
    names = []
    try:
        file = open(file_name)
        text = "".join(file.readlines)
        matches = name_regex.findall(text)
        for match in matches:
            names.append(match[1])
    except:
        print("File could not be used")
    finally:
        return names