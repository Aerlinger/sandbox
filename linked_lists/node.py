class Node(object):
  def __init__(self, value=None, next=None):
    self.next = next
    self.value = value

  def getValue(self):
    return self.value

  def setValue(self, value):
    self.value = value

  def getNext(self):
    return self.next

  def setNext(self, next):
    print self.value
    self.next = next
    return self


  def dup(self):
    return Node(self.value, self.next)

  def __str__(self):
    valstr = "(" + str(self.value) + ")"

    if self.next:
      return valstr + " -> " + str(self.next)
    else:
      return valstr

  def __cmp__(self, other):
    return cmp(self.value, other.value)
