class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        # write your code here
        node = Node(value)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            temp = self.last
            self.last.next = node
            self.last = node
        self.size +=1
            

    def dequeue(self):
        # write your code here
        #return the value of the removed node
        if self.first == None:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            self.size -=1
            if self.size == 0:
                self.last = None
            return temp.value