def diameterBinaryTree(root):
    # If there's no root, the diameter is 0
    if not root:
        return 0
    
    maxDiameter = 0
 
    # DFS function that returns the height of the tree and updates the maximum diameter
    def dfs(node):
        nonlocal maxDiameter  # allows us to modify the outer scope's maxDiameter variable
 
        # base case: if node is null, return -1 (height of an empty tree)
        if not node: 
            return -1
 
        # Time complexity for both dfs calls combined is O(n), 
        # where n is the total number of nodes in the tree,
        # because every node in the tree is visited exactly once
        leftHeight = dfs(node.left)  # calculate height of left subtree
        rightHeight = dfs(node.right)  # calculate height of right subtree
 
        # calculate diameter and update maxDiameter if current diameter is greater
        diameter = leftHeight + rightHeight + 2  # +2 because we need to count edges, not nodes
        maxDiameter = max(maxDiameter, diameter)
 
        # return height of current node
        return max(leftHeight, rightHeight) + 1  # +1 to include the current node itself
 
    # start the dfs from root
    dfs(root)
 
    # Final time complexity is O(n) as we visit each node exactly once
    return maxDiameter