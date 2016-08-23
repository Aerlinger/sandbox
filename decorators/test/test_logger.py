import unittest

from decorators.logger import log


@log("-> ")
def simpleprint(foo='bar', *args, **kwargs):
  print  "Simple print"

simpleprint(baz='qux')

print simpleprint.__name__
print simpleprint.__doc__
simpleprint
# print simpleprint.__annotations__

from classes.PatchedClass import A

a = A("foo")

a.spam()

