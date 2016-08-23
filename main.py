from decorators.splitter import splitter
from decorators.proxy import Proxy

@splitter(11)
def my_array(args):
  print "*** %s ***" % (args)
  return args

my_array(range(100))

a = 5
p = Proxy(a)

p.lol = 9

print p.lol


from functions.examples import *

splat("first", "second", "third")

keyword_args(firstkey="firstvalue", secondkey="secondvalue")
