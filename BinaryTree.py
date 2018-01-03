class BinaryTree:
    def __init__(self, num):
        self.data = Node(num)
        self.root = None

class Node:
    def __init__(self, num):
        self.data = num
        self.left = None
        self.right = None

    def printlefts(self, node):
        res = []
        res.append(node.left.data)
        if node.right:
            res += self.printlefts(node.right)
        return res

    def getfactors(self, node):
        for i in range(2, node.data + 1):
            if node.data % i == 0:
                node.left = Node(i)
                if node.data == i:
                    return node
                node.right = Node(node.data // i)
                self.getfactors(node.right)
                return node
        print('returning after for loop')

if __name__ == "__main__":
    n = Node(36)
    n = n.getfactors(n)
    # print(n.data)
    # print(n.left.data, n.right.data)
    # print(n.right.left.data, n.right.right.data)
    # print(n.right.right.left.data, n.right.right.right.data)
    # print(n.right.right.right.left.data)

    print(list(n.printlefts(n)))

