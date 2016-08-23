class TreeNode(object):
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def getValue(self):
    return self.value

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def __str__(self):
    prefix = '  ' * self.value

    buffer = "\n" + prefix + "(" +  str(self.value) + ")"

    if self.left:
      buffer += self.left.__str__()

    if self.right:
      buffer += self.right.__str__()

    return buffer



