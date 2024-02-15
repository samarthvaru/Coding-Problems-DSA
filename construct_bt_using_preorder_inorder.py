class Node:
  def __init__(self,value):
    self.val = value
    self.left = None
    self.right = None

def buildTree(preOrderTraversal, inOrderTraversal):
  if len(preOrderTraversal) == 0:
    return None
  root = Node(preOrderTraversal[0])
  index = inOrderTraversal.index(preOrderTraversal[0])
  root.left = buildTree(preOrderTraversal[1:index+1], inOrderTraversal[:index])
  root.right = buildTree(preOrderTraversal[index+1:], inOrderTraversal[index+1:])
  return root

preOrderTraversal = [5,6,8,9,7,10,11]
inOrderTraversal = [8,6,9,5,10,11,7]

a = buildTree(preOrderTraversal,inOrderTraversal)