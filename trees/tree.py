def num_nodes(root):
  if root is None:
    return 0

  return 1 + num_nodes(root.left) + num_nodes(root.right)

def is_k_balanced(root, k = 0):
  return abs(balance(root)) <= k

def children_are_k_balanced(root, k):
  is_k_balanced(root.left, k) and is_k_balanced(root.right, k)

def find_k_unbalanced(root, k=1):
  if root is None:
    return

  if not is_k_balanced(root, k):
    return root

  left_unbalanced = find_k_unbalanced(root.left, k)
  right_unbalanced = find_k_unbalanced(root.right, k)

  return left_unbalanced or right_unbalanced

def find_k_balanced(root, k=1):
  if root is None:
    return

  if is_k_balanced(root, k):
    return root

  left_balanced = find_k_balanced(root.left, k)
  right_balanced = find_k_balanced(root.right, k)

  return left_balanced or right_balanced

def inorder(root):
  if root == None:
    return

  inorder(root.left)

  print(root.value, num_nodes(root), balance(root))


  inorder(root.right)
