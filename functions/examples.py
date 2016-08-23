import itertools

def splat(*args):
  for arg in args:
    print arg

def keyword_args(**args):
  for key, value in args.iteritems():
    print "<%s> : %s" % (key, value)

# def requires_keyword_args(maxsize, *, block):
#   print maxsize, block
