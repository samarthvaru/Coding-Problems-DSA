class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def checkLoop(head):
    #write your code here
    if not head or not head.next:
        return None
    
    hare = head
    tortoise = head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            break
    
    if hare!=tortoise:
        return None
    
    pointer = head
    while pointer!=tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
    
    return tortoise