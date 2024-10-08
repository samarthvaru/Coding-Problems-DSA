from collections import defaultdict

def checkCycle(edges):
    adj_list = defaultdict(list)

    # Building the adjacency list for the graph
    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visit = set()

    # Helper function for DFS traversal
    def dfs(node, parent):
        # If the node is already visited, check if it's not the parent (indicating a cycle)
        if node in visit:
            return True

        visit.add(node)

        # Visit all the neighbors
        for nei in adj_list[node]:
            if nei != parent:  # Only visit neighbors that are not the parent
                # Recur for the neighbors
                if dfs(nei, node):
                    return True

        return False

    # Check each node in case the graph is disconnected
    for i in range(len(adj_list)):
        if i not in visit:
            if dfs(i, -1):
                return True

    return False


# Test Cases
V = 4
edges = [[0, 1], [1, 2], [2, 3]]
V = 5
edges2 = [[0, 1], [1, 2], [2, 0], [1, 3]]

print(checkCycle(edges))   # Expected Output: False
print(checkCycle(edges2))  # Expected Output: True
