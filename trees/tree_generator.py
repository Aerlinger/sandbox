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
ll = TreeNode(3, None, lll)
lr = TreeNode(3)

l = TreeNode(2, ll, lr)
rr = TreeNode(7)
r = TreeNode(2, rr)

asym_root = TreeNode(1, l, r)

x = TreeNode(0, None, asym_root)

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

def flat_print(root):
  if root is None:
    return

  flat_print(root.left)
  print("(", root.value, ")")
  flat_print(root.right)

def leaves(root):
  if not root:
    return []

  # We're at a leaf node
  if not root.left and not root.right:
    return [root]

  return leaves(root.left) + leaves(root.right)

def left_edge(root):
  if not root:
    return []

  return [root] + left_edge(root.left)


def right_edge(root):
  if not root:
    return []

  return [root] + left_edge(root.left)

def get_sum(root, path=(), total = 0):
  if not root:
    return {}

  path = path + (root,)
  total = total + root.value

  if root.left is None and root.right is None:
    return { path: total }

  left_sums = get_sum(root.left, path, total)
  right_sums = get_sum(root.right, path, total)

  return {**left_sums, **right_sums}


print(leaves(asym_root))
print(leaves(root))
print(())
print(asym_root)
print("SUM", get_sum(root))
print("SUM", get_sum(asym_root))
# print("Leaves", asym_root)
# print("Leaves", root)

def invert_dict(my_map):
  inv_map = {}

  for k, v in my_map.items():
    inv_map.setdefault(v, []).append(k)

  return inv_map

print(invert_dict(get_sum(root)))
print(invert_dict(get_sum(asym_root)))


def preorder(root, f):
  if root is None:
    return

  f(root)
  preorder(root.left, f)
  preorder(root.right, f)

def inorder(root, f):
  if root is None:
    return

  inorder(root.left, f)
  f(root)
  inorder(root.right, f)

def postorder(root, f):
  if root is None:
    return

  postorder(root.left, f)
  postorder(root.right, f)
  f(root)

def process(node):
  print(node.value)


def depth(root, initial=0):
  if root is None:
    return 0

  return 1 + max(depth(root.left), depth(root.right))

def depth_map(root, total=0):
  depth = total + 1

  if root is None:
    return (depth, None)

  left_map = depth_map(root.left, depth)
  right_map = depth_map(root.right, depth)

  this_map = (depth, root)

  return this_map, left_map, right_map

def bfs(root, f):
  queue = [root]
  buffer = []

  net = 0

  while len(queue) > 0:
    print("Q", queue[0].value, ":", queue, net, queue[0].numChildren())

    current_node = queue.pop(0)
    net -= 1

    # f(current_node)

    if current_node.left:
      net += 1
      queue.append(current_node.left)

    if current_node.right:
      net += 1
      queue.append(current_node.right)



print("PREORDER")
preorder(asym_root, lambda x: print(x.value))

print("INORDER")
inorder(asym_root, lambda x: print(x.value))

print("POSTORDER")
postorder(asym_root, lambda x: print(x.value))

print("BFS")
print(x)
bfs(x, lambda x: print(x.value))

print("DEPTH")
print(depth_map(x))

print("BFS Root")
print(root)
bfs(root, lambda x: print(x.value))

from linked_lists.node import Node

def leaves_to_ll(root):
  if not root:
    return None

  # We're at a leaf node
  if not root.left and not root.right:
    return Node(root.value)

  head = leaves_to_ll(root.left)
  tail = leaves_to_ll(root.right)

  if head:
    tail_of_head = head.getTail()
    tail_of_head.next = tail

    return head
  else:
    return tail

def left_edge_to_ll(root):
  if not root:
    return

  if root.left is None:
    return Node(root.value, left_edge_to_ll(root.right))
  else:
    return Node(root.value, left_edge_to_ll(root.left))

def right_edge_to_ll(root, path = None):
  if not root:
    return

  if root.right is None:
    return Node(root.value, right_edge_to_ll(root.left))
  else:
    return Node(root.value, right_edge_to_ll(root.right))
#
# def right_edge_to_ll(root, path = None):
#   if not root.right:
#     return Node(root.value)
#
#   n = Node(root.value)
#   return right_edge_to_ll(root.right).setNext(n)

def perimeter(root):
  left_edge = left_edge_to_ll(root)
  leaves = leaves_to_ll(root)
  right_edge = right_edge_to_ll(root)

  left_edge_tail = left_edge.getTail()
  leaves_tail = leaves.getTail()

  left_edge_tail.setNext(leaves.getNext())
  leaves_tail.setNext(right_edge.getNext())

  return left_edge

def remove(node, ll):
  iter = ll
  prev_iter = None

  while iter:
    next_iter = iter.next

    if (iter.value == node.value):
      if prev_iter:
        prev_iter.next = next_iter

      iter.next = None
      return iter

    prev_iter = iter
    iter = next_iter

  return None

def union(left, right):
  temp_l = left
  temp_r = right

  head = None
  current_head = head

  # Def copy?
  while temp_l and temp_r:
    if temp_l.value is not temp_r.value:
      if head is None:
        head = temp_r
        current_head = head

      current_head.next = Node(temp_r.value)

    temp_l = temp_l.next
    temp_r = temp_r.next

  return current_head

le = left_edge_to_ll(x)
re = right_edge_to_ll(x)

print("TAIL", left_edge_to_ll(x).getTail())
print("LEFT EDGE", left_edge_to_ll(x))
print("LEAVES", leaves_to_ll(x))
print("RIGHT EDGE", right_edge_to_ll(x))

print("UNION", union(le, re))
print("depth", depth(x))
print("depth", depth(root))
print("depth", depth(asym_root))

# print("PERIM", perimeter(asym_root))
# print("PERIM", perimeter(root))
