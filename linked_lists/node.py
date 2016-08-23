class Node(object):
  def __init__(self, value=None, next=None, prev=None):
    self.next = next
    self.prev = prev
    self.value = value

  def getValue(self):
    return self.value

  def setValue(self, value):
    self.value = value

  def getPrev(self):
    return self.prev

  def setPrev(self, prev):
    self.prev = prev
    return self

  def getNext(self):
    return self.next

  def setNext(self, next):
    self.next = next
    return self

  def getTail(self):
    tail = self

    while tail.next is not None:
      tail = tail.next

    return tail

  def dup(self):
    return Node(self.value, self.next)

  def __str__(self):
    valstr = "(" + str(self.value) + ")"

    arrow_sym = "-->"
    prev_value = ""

    if self.prev:
      arrow_sym = "<->"
      prev_value = self.prev.value

    if self.next:
      return prev_value + valstr + arrow_sym + str(self.next)
    else:
      return prev_value + valstr

  def __cmp__(self, other):
    return cmp(self.value, other.value)



