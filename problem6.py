sumofsquare = 0
for i in range(1, 101):
    sumofsquare += i**2

sums = 0
for i in range(1, 101):
    sums += i
squareofsums = sums ** 2
print(squareofsums - sumofsquare)
