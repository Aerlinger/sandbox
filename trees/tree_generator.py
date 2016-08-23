from trees.tree_node import TreeNode
import random

def generate_tree(depth = 5):
  root = Node(0)

def construct_branches(depth):
  if depth == 0:
    return None

  left = construct_branches(depth-1)

  if random.randint(0, 1) > 0:
    right = construct_branches(depth-1)
  else:
    right = None

  return TreeNode(depth, left, right)


root = construct_branches(5)

def num_nodes(root):
  if root is None:
    return 0

  return 1 + num_nodes(root.left) + num_nodes(root.right)

def balance(root):
  if root is None:
    return 0

  return num_nodes(root.right) - num_nodes(root.left)

def postorder(root):
  balance

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

def find_n_k_balanced(root, n, k):
  first_k_imbalanced = find_k_unbalanced(asym_root, n)

  return find_k_balanced(first_k_imbalanced, k)

def has_node(root, node):
  if root is None or node is None:
    return

  if root == node:
    return node

  return has_node(root.left, node) or has_node(root.right, node)


print(root)
print("numnodes", num_nodes(root))
print("balance", balance(root))


# Asymmtrical tree:

lll = TreeNode(4)
ll = TreeNode(3, lll)
lr = TreeNode(3)

l = TreeNode(2, ll, lr)
r = TreeNode(2, None)

asym_root = TreeNode(1, l, r)

print("\nPredefined tree")
print(asym_root)

print("numnodes", num_nodes(asym_root))
print("balance", balance(asym_root))

print("0 balanced", find_k_balanced(asym_root, 0))
print("1 balanced", find_k_balanced(asym_root, 1))
print("2 balanced", find_k_balanced(asym_root, 2))
print("3 balanced", find_k_balanced(asym_root, 3))

print("0 unbalanced", find_k_unbalanced(asym_root, 0))
print("1 unbalanced", find_k_unbalanced(asym_root, 1))
print("2 unbalanced", find_k_unbalanced(asym_root, 2))
print("3 unbalanced", find_k_unbalanced(asym_root, 3))

print("0 nk balanced", find_n_k_balanced(asym_root, 2, 0))
print("1 nk balanced", find_n_k_balanced(asym_root, 2, 1))
print("2 nk balanced", find_n_k_balanced(asym_root, 2, 2))
print("3 nk balanced", find_n_k_balanced(asym_root, 2, 3))

print("root has lll?", has_node(asym_root, lll))
print("ll has lll?", has_node(ll, lll))
print("lll has ll?", has_node(lll, ll))
print("l has r?", has_node(l, r))
print("l has l?", has_node(l, l))

def lca(root, a, b):
  if root is None or a is None or b is None:
    return root


  # If this node has both a and b as descendents, but either of it's children don't, we're at the LCA
  if (has_node(root, a) and has_node(root, b)):
    left_has_children = has_node(root.left, a) and has_node(root.left, b)
    right_has_children = has_node(root.right, a) and has_node(root.right, b)

    if left_has_children == right_has_children:
      return root

    else:
      return lca(root.left, a, b) or lca(root.right, a, b)

print("LCA l: l, r", lca(l, l, r))
print("LCA, lll, lr", lca(asym_root, lll, lr))
print("LCA, lll, ll", lca(asym_root, lll, ll))
print("LCA, l, r", lca(asym_root, l, r))
print("LCA, lll, r", lca(asym_root, lll, r))


