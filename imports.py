from a_package import a_class
import a_package

foo = a_class.Foo()
foo2 = a_package.a_class.Foo()

print a_package.__author__
print foo.name
print foo2.name

classy = a_package.ClassInInit()

classy.speak()

import modules.main as p

from modules.submodule.BasicClass import OldStyleClass
from modules.submodule.BasicClass import BasicClass

b = BasicClass()


print str(b)

b

