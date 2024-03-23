from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, array):
        #write code here
        if(len(array)==0):
            return
        i = 0
        
        #if root is null
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i+=1
                if i == len(array):
                    return self
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            
            #process left child
            if current.left is None:
                if array[i] is not None:
                    node= Node(array[i])
                    current.left = node
                i+=1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)

            #process right child
            if current.right is None:
                if array[i] is not None:
                    node= Node(array[i])
                    current.right = node
                i+=1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)           
            
            
        #return self once you are done

def level_order_traversal(root):
    if root is None:  
        return []

    output = []
    queue = deque([root])
    
    while queue:
        length = len(queue)
        count = 0
        curr_level_values = []
        
        while count < length:
            curr = queue.popleft()
            curr_level_values.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
                
            count+=1
        
        output.append(curr_level_values)

    #write your code here

    return output        

#For you to test by yourself
# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])