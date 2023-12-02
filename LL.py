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
        oldTail = self.tail
        oldTail.next = temp
        self.tail = temp
        self.count += 1


ll = LL(4)
ll.appendToLL(55)
ll.printLL()
print(ll.tail.value)
print(ll.count)
