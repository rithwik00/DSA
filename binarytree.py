class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:

            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def printTree(self):

        if self.left:
            self.left.printTree()
        print(self.data)

        if self.right:
            self.right.printTree()


    def inOrderTraversal(self, root): # left root right
        res = []

        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res += self.inOrderTraversal(root.right)
        return res

    def preOrderTraversal(self, root): # root left right
        res = []

        if root:
            res.append(root.data)
            res += self.inOrderTraversal(root.left)
            res += self.inOrderTraversal(root.right)
        return res

    def postOrderTraversal(self, root): # left right root
        res = []

        if root:
            res = self.inOrderTraversal(root.left)
            res += self.inOrderTraversal(root.right)
            res.append(root.data)
        return res

data_list = [12, 6, 14, 3, 7, 2, 8, 10]

root = Node(data_list[0])

for i in data_list[1:]:
    root.insert(i)

print(*root.inOrderTraversal(root))
print(*root.preOrderTraversal(root))
print(*root.postOrderTraversal(root))