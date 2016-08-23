class Proxy:
  def __init__(self, obj):
    self._obj = obj

  def __getattr__(self, item):
    print "Got attr: ", item.__name__
    print "value: ", item

  def __set_attr__(self, item):
    print "Set attr: ", item.__name__
    print "value: ", item
