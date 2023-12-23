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

    def prependToLL(self, value):
        newNode = Node(value)
        if self.count == 0:
            print("\numty LL")
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.count += 1
        return True
    
    def popFirst(self):
        if self.count == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.count -= 1
        if self.count == 0:
            self.tail = None
        return temp

    def getNode(self, index):
        if index < 0 or index >= self.count: #covers any -integer and out of bound and also when accessing 0 for empty LL
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def setValue(self, index, value):
        temp = self.getNode(index)
        if temp:
            temp.value = value
            return True
        return False

    def insertNode(self, index, value):
        newNode = Node(value)
        if index < 0 or index > self.count:
            return False
        elif index == 0:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            return True
        preIndex = index - 1
        temp = self.head
        for _ in range(preIndex):
            temp = temp.next
        temp2 = temp.next
        temp.next = newNode
        newNode.next = temp2
        return True

    def reverseLL(self):
        if self.count == 0:
            print("empty LL, no reverse possible")
        elif self.count == 1:
            print("Only 1 node, no reverse possible")
        else:
            prev = None
            current = self.head
            while(current):
                if prev == None:
                    self.tail = current
                if current.next == None:
                    self.head = current
                temp = current.next
                current.next = prev
                prev = current
                current = temp

ll = LL(4)
ll.appendToLL(55)
ll.appendToLL(11)
ll.appendToLL(23)
ll.printLL()
ll.reverseLL()
print("")
ll.printLL()
























#node2 = ll.getNode(0)
#print(node2.value if node2 != None else "Index out of bound" )
#print("popped",ll.popFromLL().value)
#print("after popped: ")
#ll.printLL()
#print("")
#print(ll.tail.value)
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