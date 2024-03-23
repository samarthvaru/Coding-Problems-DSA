class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
 
def linkNodes(node1, node2):
    node1.next = node2
    node2.prev = node1
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
 
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
 
        node.next = None
        node.prev = None
 
    def insertB(self, nodePosition, nodeInsert):
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
        self.remove(nodeInsert)
 
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition
 
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
        nodePosition.prev = nodeInsert
 
    def allNodesValueRemove(self, value):
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            if temp.val == value:
                self.remove(temp)
 
    def insertPosition(self, position, node):
        # Time complexity Explanation:
        # This method involves traversing the list until the desired position or the end of the list is reached.
        # Therefore, the time complexity is linear O(n), where n is the number of nodes in the list.
 
        curr = self.head
        counter = 0
        while curr != None and counter != position:
            curr = curr.next
            counter += 1
        if curr != None:
            self.insertB(curr, node)
        else:
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.remove(node)
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node