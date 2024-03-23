class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self

def add2Numbers(l1, l2):
    #write your code here
    carryForward = 0
    results = LinkedList()
    while l1 or l2 or carryForward:
        l1Value = l1.value if l1 else 0
        l2Value = l2.value if l2 else 0
        sum = (l1Value + l2Value+carryForward)
        nodeValue = sum%10
        results.addAtTail(nodeValue)
        carryForward = sum//10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return results