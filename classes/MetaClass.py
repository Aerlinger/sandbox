class NoInstances(type):
  def __new__(meta, name, bases, dct):
    print '-----------------------------------'
    print "Allocating memory for class", name
    print meta
    print bases
    print dct
    return super(NoInstances, meta).__new__(meta, name, bases, dct)

  def __init__(cls, name, bases, dct):
    print '-----------------------------------'
    print "Initializing class", name
    print cls
    print bases
    print dct
    super(NoInstances, cls).__init__(name, bases, dct)

  def __call__(self, *args, **kwargs):
    print '-----------------------------------'
    print "Calling"
    print cls
    type.__call__(self, *args, **kwargs)

class Spam():
  __metaclass__ = NoInstances

  @staticmethod
  def grok(x):
    print 'Spam.grok: ', x

print "TYPE"
print type(Spam)
print type(type(Spam))

Spam.grok("Example")

s = Spam()
