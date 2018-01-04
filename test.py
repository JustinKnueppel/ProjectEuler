import os, shutil, re
regex = re.compile(('''
        (.*\D)
        (\d)
        (\D.*)
        '''),re.VERBOSE)
for i in os.listdir():
    matchs = regex.search(i)
    if matchs:
        print(matchs.group())
        print(matchs.groups())
        newn = matchs.group(1) + "0" + matchs.group(2) + matchs.group(3)
        print(newn)
        shutil.move(matchs.group(), newn)
