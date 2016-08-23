from linked_lists.node import Node

left_q = Node('q')
left_m = Node('m', left_q)
left_c = Node('b', left_m)
left_b = Node('b', left_c)

print str(left_b)


right_t = Node('t')
right_q = Node('q', right_t)
right_n = Node('n', right_q)
right_d = Node('d', right_n)
right_b = Node('b', right_d)
right_a = Node('a', right_b)

print str(right_a)


def merge(left, right):
  if left is not None and left <= right:
    nextNode = merge(left.getNext(), right)
    return Node(left.getValue(), nextNode)

  elif right is not None:
    nextNode = merge(left, right.getNext())
    return Node(right.getValue(), nextNode)

  else:
    return None

print "MERGE"
print merge(left_b, right_a)

'''
def reverse(head):
  if head.getNext() is None:
    print head
    return head.dup()
  else:
    new_head = reverse(head.getNext())
    print head

    return new_head.next()

    # return new_head()


def root_reverse(head):
  reversed = reverse(head)
  head.setNext(None)

  return head


print "REVERSE"

print reverse(left_b)

# print left_q
# print left_m
# print left_c
# print left_b
'''

cyclic_t = Node('t')
cyclic_q = Node('q', cyclic_t)
cyclic_n = Node('n', cyclic_q)
cyclic_d = Node('d', cyclic_n)
cyclic_b = Node('b', cyclic_d)
cyclic_a = Node('a', cyclic_b)

cyclic_t.setNext(cyclic_q)


def is_cyclic(head, visited = []):
  if head in visited:
    return True

  if head.getNext() is None:
    return False

  return is_cyclic(head.getNext(), visited + [head])

print is_cyclic(cyclic_t)
print is_cyclic(right_t)

