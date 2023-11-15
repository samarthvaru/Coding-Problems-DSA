class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    #write code here
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
reverseLinkedList(head)