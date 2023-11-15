def invertRecursive(node):
    if node is None:  # Check if node is null (Time Complexity: O(1))
        return
 
    # Swap the nodes (Time Complexity: O(1))
    temp = node.left
    node.left = node.right
    node.right = temp
 
    # Perform the same operations for the left and right child nodes
    invertRecursive(node.left)  # Recursive call (Time Complexity: T(n/2))
    invertRecursive(node.right)  # Recursive call (Time Complexity: T(n/2))
 
    # Therefore, the overall Time Complexity of the function is O(n),
    # where n is the total number of nodes in the binary tree. This is because
    # each node in the tree is visited exactly once.
    return node