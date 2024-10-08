from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_right_leaves(root: TreeNode) -> int:
    if not root:
        return 0

    total_sum = 0
    stack = deque()
    current = root

    while stack or current:
        # Traverse to the left subtree
        while current:
            stack.append(current)
            current = current.left

        # Process the node
        current = stack.pop()

        # Check if the left child is a leaf node
        if current.right and not current.right.left and not current.right.right:
            total_sum += current.right.val

        # Move to the right subtree
        current = current.right

    return total_sum

# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(9)

print(sum_of_right_leaves(root))  # Output: 2
