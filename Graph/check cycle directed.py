from collections import defaultdict

def checkCycleDirected(edges, V):
    adj_list = defaultdict(list)

    # Building the adjacency list for the directed graph
    for src, dst in edges:
        adj_list[src].append(dst)

    visit = set()        # Set to track visited nodes
    rec_stack = set()    # Set to track the current recursion stack

    # Helper function for DFS traversal
    def dfs(node):
        # If the node is in the recursion stack, we found a cycle
        if node in rec_stack:
            return True

        # If the node has already been fully processed, skip it
        if node in visit:
            return False

        # Mark the node as visited and add to the recursion stack
        visit.add(node)
        rec_stack.add(node)

        # Visit all the neighbors
        for nei in adj_list[node]:
            if dfs(nei):
                return True

        # Remove the node from the recursion stack after exploring its neighbors
        rec_stack.remove(node)

        return False

    # Check for cycles starting from each node
    for i in range(V):
        if i not in visit:
            if dfs(i):
                return True

    return False


# Test Cases for a directed graph
V = 4
edges_directed = [[0, 1], [1, 2], [2, 3], [3, 1]]  # Cycle exists
edges_no_cycle = [[0, 1], [1, 2], [2, 3]]  # No cycle

print(checkCycleDirected(edges_directed, V))   # Expected Output: True
print(checkCycleDirected(edges_no_cycle, V))   # Expected Output: False