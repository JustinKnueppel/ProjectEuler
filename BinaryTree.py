class BinaryTree:
    def __init__(self, num):
        self.data = Node(num)
        self.root = None

class Node:
    def __init__(self, num):
        self.data = num
        self.left = None
        self.right = None

    @classmethod
    def makegridnode(cls, side = 2):
        return cls((side, side))

    #used to find possible grid paths for problem 15
    def findgridpaths(self, node):
        if node.data == (0,0):
            return
        if node.data[0] is not 0:
            newn = Node((node.data[0] - 1, node.data[1]))
            node.left = self.findgridpaths(newn)
        if node.data[1] is not 0:
            newn = Node((node.data[0], node.data[1] - 1))
            node.right = self.findgridpaths(newn)
        return node

    def countheads(self, node):
        if node.left == None and node.right == None:
            return 1
        counter = 0
        if node.left:
            counter += self.countheads(node.left)
        if node.right:
            counter += self.countheads(node.right)
        return counter

    def getlefts(self, node):
        res = []
        res.append(node.left.data)
        if node.right:
            res += self.getlefts(node.right)
        return res

    #puts all prime factors on left nodes
    def getfactors(self, node):
        for i in range(2, node.data + 1):
            if node.data % i == 0:
                node.left = Node(i)
                if node.data == i:
                    return node
                node.right = Node(node.data // i)
                self.getfactors(node.right)
                return node

    def getpossibleroutes(self, gridnode):
        #go through possible lefts, then rights
        print(node.data)

if __name__ == "__main__":
    print('running BinaryTree')
    for i in range(1, 13):
        nod = Node.makegridnode(i)
        print(nod.data)
        nod = nod.findgridpaths(nod)
        print(nod.countheads(nod))
