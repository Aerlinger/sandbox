from trees.tree_node import TreeNode
import random

lll = TreeNode(4)


def make_tree(n):
  if n == 1:
    return TreeNode(n)

  left_side = make_tree(n/2)
  right_side = make_tree(n/2)

  left_side

lll = TreeNode(1)
ll = TreeNode(2, lll, None)
lrl = TreeNode(4)
lr = TreeNode(5, lrl)

l = TreeNode(3, ll, lr)
rr = TreeNode(8)
r = TreeNode(7, None, rr)

asym_root = TreeNode(6, l, r)

x = TreeNode(0, None, asym_root)

# print("\nPredefined tree")
# print(asym_root)

def is_leaf(node):
  return node.left == None and node.right == None


def traverse(root, history = []):
  if root ==  None:
    return

  if root.left == None and root.right == None:
    print("LEAF", root.value)

  print("PRE", root.value)

  traverse(root.left)
  # print("IN", root.value)

  traverse(root.right)
  print("POST", root.value)

def perimeter(root):
  pass

def left_perimeter(root):
  if root is None:
    return 0

  if root.left:
    return 1 + left_perimeter(root.left) + num_leaves(root.right)

  return 1

def right_perimeter(root):
  if root.right:
    return 1 + right_perimeter(root.right) + num_leaves(root.left)

  else:
    return 1

def num_leaves(root):
  if root is None:
    return 0

  if root.left == None and root.right == None:
    return 1

  left_leaves = 0
  if root.right:
    left_leaves = num_leaves(root.right)

  right_leaves = 0
  if root.left:
    right_leaves = num_leaves(root.left)

  return left_leaves + right_leaves

# traverse(asym_root)
# print(num_leaves(asym_root))
# print(left_perimeter(asym_root.left))
# print(right_perimeter(asym_root.right))

def maximum(node):
  if node is None:
    return 0

  if node.right is None:
    return node.value

  return maximum(node.right)

def inorder(node):
  if node is None:
    return

  # #Leaf node:
  # if node.left is None and node.right is None:
  #   return

  inorder(node.left)
  print(node.value)
  inorder(node.right)

# EPI 10.8
def count(node, k = 0):
  if node is None:
    return 0

  if node.left is None and node.right is None:
    print("k =", k + 1, "  val = ", node.value)
    return 1

  left_count = count(node.left, k)

  node_value = k + left_count + 1
  print("k =", node_value, "  val = ", node.value)

  right_count = count(node.right, node_value)

  return left_count + right_count + 1

def kth_inorder(node, k=0):
  if node is None:
    return k

  # left_value = kth_inorder(node.left, k)
  left_value = count(node.left)

  node_value = left_value + 1

  print("k =", node_value, "  val = ", node.value)

  kth_inorder(node.right, node_value)

  return node_value

# EPI 10.7
def find_by_sum(node, target_sum, accum = 0):
  if not node:
    return []

  sum_so_far = accum + node.value

  if is_leaf(node):
    if sum_so_far == target_sum:
      return [node]

  left_result = find_by_sum(node.left, target_sum, accum + node.value)
  right_result = find_by_sum(node.right, target_sum, accum + node.value)

  if left_result:
    return [node] + left_result

  if right_result:
    return [node] + right_result

# find_by_sum(node, target_sum, accum=0):

# inorder(asym_root)
# print(kth_inorder(asym_root, 0))

# print(maximum(asym_root.left.left))
# print(maximum(asym_root.left))
# print(maximum(asym_root))

# print(count(asym_root.left.left))
# print(count(asym_root.left))
# print(count(asym_root))

# print(find_by_sum(asym_root, 12, accum=0))

def process_node(stack, node):
  current_node = stack.pop()

  return current_node

# 10.10
def iterative_inorder(root):
  stack = []

  head = root
  stack.append(head)

  while len(stack) > 0:
    print("S", stack)

    if head.left:
      head = head.left
      stack.append(head)
    else:
      current_node = stack.pop()
      print("L", current_node.value)

      if head.right:
        head = head.right
        stack.append(head)
      else:
        current_node = stack.pop()
        print("R", current_node.value)


def iterative_inorder(root):
  stack = []
  processed = []

  head = root
  stack.append(head)

  while len(stack) > 0:
    # print("S", stack, "P", processed)

    if head.left is None or head.left in processed:
      print("-- ", head.value," -- L current node", head.value, " is either a terminal node or it has already been processed. It will be processed and dequeued", stack)
      stack.pop()
      processed.append(head)

      if head.right and head.right not in processed:
        stack.append(head.right)
        print("Node", head.value, " has right child", head.right.value, "it is added to the stack: ", stack, "(processed)", processed)
        head = head.right
      else:
        print("Node", head.value, "has no right child either, it is processed and removed from the stack: ", stack, "(processed)", processed)
        processed.append(head)

        if len(stack) > 0:
          stack.pop()
          head = stack[-1]

    else:
      print("I haven't seen L node", head.value, "yet, so I add it to the stack: ", stack)
      head = head.left
      stack.append(head)

iterative_inorder(asym_root)

  # while(len(queue) > 0):
  #   root.left



