class Node:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def inOrder(root):
  if root is None:
    return None
  inOrder(root.left)
  print(str(root.val) + "->", end=' ')
  inOrder(root.right)


def insert(root, val):
  if root is None:
    return Node(val)
  if val < root.val:
    root.left = insert(root.left, val)
  else:
    root.right = insert(root.right, val)

  return root


def minValue(root):
  current = root
  while current.left is not None:
    current = current.left
  return current.val


def search(root, val):
  if root is None:
    return False
  if root.val == val:
    return True
  if val < root.val:
    return search(root.left, val)
  else:
    return search(root.right, val)


def delete(root, val):
  if root is None:
    return root
  if val < root.val:
    root.left = delete(root.left, val)
  elif val > root.val:
    root.right = delete(root.right, val)
  else:
    if root.left is None:
      temp = root.right
      root = None
      return temp
    elif root.right is None:
      temp = root.left
      root = None
      return temp
    temp = minValue(root.right)
    root.val = temp.val
    root.right = delete(root.right, temp)

  return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inOrder(root)

print("\nDelete 10")
root = delete(root, 10)
print("Inorder traversal: ", end=' ')
inOrder(root)
