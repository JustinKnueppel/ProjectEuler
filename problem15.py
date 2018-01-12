# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# use binary tree and count the tips
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getnumpaths(self, node):
        if node.data[0] == 0 or node.data[1] == 0:
            node.left = None
            node.right = None
            return node
        if node.data[0] is not 0:
            newn = Node((node.data[0]-1, node.data[1]))
            node.left = self.getnumpaths(newn)
        if node.data[0] is not node.data[1] and node.data[1] is not 0:
            newn = Node((node.data[0], node.data[1]-1))
            node.right = self.getnumpaths(newn)
            # Only make the right node if if the data is not a square
        return node

    def countgridheads(self, node):
        if node.left == None and node.right == None:
            return 1
        counter = 0
        if node.data[0] == node.data[1]:
            counter += 2 * self.countgridheads(node.left)
        elif node.left and node.right:
            counter += self.countgridheads(node.right)
            counter += self.countgridheads(node.left)
        return counter

import time
# Use recursive binary tree will crash attempting 20, better math solution below

# sizesq = 5
# obj = Node((sizesq - 1, sizesq))
# st2 = time.time()
# obj = obj.getnumpaths(obj)
# print(2 * obj.countgridheads(obj))
# end2 = time.time()
# dif2 = end2 - st2
# print(dif2)

def getposgrid(gridsize):
    tally = [1] * gridsize
    for i in range(gridsize):
        for j in range(i):
            tally[j] += tally[j-1]
        tally[i] = 2 * tally[i-1]
    return tally[gridsize - 1]

for i in range(1, 21):
    start = time.time()
    print(getposgrid(i))
    end = time.time() - start
    print(end)

