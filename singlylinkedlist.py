class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class SlinkedList():
    def __init__(self,head = None):
        self.head = head

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insertend(self,data):
        node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def insertbeg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertmiddle(self,node,data):
        temp = Node(data)
        temp.next = node.next
        node.next = temp

    def remove(self,data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
        temp1 = None
        while temp is not None:
            if temp.data == data:
                temp1.next = temp.next
            temp1 = temp
            temp = temp.next



    
list1 = SlinkedList(Node('mon'))
e2 = Node('tue')
e3 = Node('wed')
list1.head.next = e2
e2.next = e3
list1.insertbeg('sun')
list1.insertend('thu')
list1.insertend('fri')
list1.insertend('sat')
list1.insertmiddle(e3,'funday')
list1.print()
print('|||after deletion of key="funday"|||')
list1.remove('funday')
list1.print()

#######################################################
