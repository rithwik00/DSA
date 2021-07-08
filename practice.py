class Node:

    def __init__(self, data):
        self.right = None
        self.left = None
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


data_list = [12, 6, 14, 3, 7, 2, 8, 10]

root = Node(data_list[0])

for i in data_list[1:]:
    root.insert(i)

root.printTree()