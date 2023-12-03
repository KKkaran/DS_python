from Node import Node

class LL:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.count = 1

    def printLL(self):
        node = self.head
        while node is not None:
            print (node.value)
            node = node.next

    def appendToLL(self, value):
        temp = Node(value)
        self.count += 1
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def popFromLL(self):
        temp = self.head
        



ll = LL(4)
ll.appendToLL(55)
ll.appendToLL(11)
ll.appendToLL(23)
#ll.printLL()
print(ll.tail.value)