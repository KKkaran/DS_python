from Node import Node

class LL:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.count = 1

    def printLL(self):
        if self.count == 0:
            print("nothin 2 print. empty ll")
        node = self.head
        while node is not None:
            print (node.value, end="-->")
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
        if self.count == 0:
            return None
        elif self.count == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.count = 0
            return temp
        temp = self.head
        while temp.next is not None:
            if temp.next.next is None:
                popped = temp.next
                self.tail = temp
                temp.next = None
                self.count -= 1
                return popped
            else:
                temp = temp.next
#  head                 tail
#   4      55    11      23
#  head         tail
#   4      55    11

ll = LL(4)
ll.appendToLL(55)
ll.appendToLL(11)
ll.appendToLL(23)
ll.printLL()
print("")
print("popped",ll.popFromLL().value)
print("after popped: ")
ll.printLL()
print("")
print(ll.tail.value)
# print("")
# ll.popFromLL()
# ll.printLL()
# print("")
# ll.popFromLL()
# ll.printLL()
# print("")
# ll.popFromLL()
# ll.printLL()
# print("")
# ll.popFromLL()
# ll.printLL()
# ll.appendToLL(101)
# ll.printLL()