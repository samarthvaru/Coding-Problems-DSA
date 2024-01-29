# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        count = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == 1:
            return head
        
        mid = int(math.floor(length / 2))
    
        while head:
            count += 1
            head = head.next
            if count == mid:
                return head
            
        return None