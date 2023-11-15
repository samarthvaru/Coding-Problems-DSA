from collections import deque
 
def invertIterative(root):
    if root is None: 
        return # No operation required if root is None, hence O(1) time complexity.
    
    queue = deque([root]) # We use a queue for bfs of the tree. 
    
    while queue: # This loop runs once for each node in the tree, hence O(n) time complexity, where n is the number of nodes.
        current = queue.popleft() # This operation takes O(1) time in Python deque.
        current.left, current.right = current.right, current.left # Swapping takes O(1) time.
        if current.left: 
            queue.append(current.left) # This operation takes O(1) time.
        if current.right: 
            queue.append(current.right) # This operation takes O(1) time.
    
    return root # This operation takes O(1) time.
 
# Final time complexity: O(n), where n is the number of nodes in the tree.