# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        output = []
        queue = deque([root])

        while queue:

            length = len(queue)
            count = 0
            curr_level_val = []

            while count < length:
                curr = queue.popleft()
                curr_level_val.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                count+=1
            
            output.append(curr_level_val)

        return output        