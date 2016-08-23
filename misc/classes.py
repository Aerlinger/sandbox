class Animal:
    '''
    An animal definition:
    '''

    print 'Animal class definition has been created.'

    def __init__(self, name='animal name'):
        self.name = name

    def speak(self):
        print self.name

    def classMethod(cls):
        print 'this is a class method'

genericAnimal = Animal()
print genericAnimal.name

bob = Animal('Bob')
print bob.name



class Dog(Animal):

    print 'Animal class definition has been created.'
    def __init__(self):
        self.name = 'Sparky'

dog = Dog()


print ""
print ""


# Dog object:
class Dog2(object):
    def __init__(self):
        self._name = None

    def set_name(self, a_name):
        print "Setting name to " + a_name
        self._name = a_name

    def get_name(self):
        print "getting name"
        return self._name

    name = property(get_name, set_name)
    description = property(get_name, set_name)

fido = Dog2()

fido.name = "fido"
fido.description = "Fido"

print fido.description
print fido.name

print ""
print ""


class Dog3(object):

    def __init__(self):
        self._name = None

    @property
    def name(self):
        print "getting name"
        return self._name

    @name.setter
    def name(self, name):
        print "Setting name to " + name
        self._name = name

    @property
    def description(self):
        print "Getting description"
        return self._description

    @description.setter
    def description(self, description):
        print "Setting description to " + description
        self._description = description

sparky = Dog3()

sparky.name = "sparky"
a = sparky.name
sparky.description = "a dog"
a = sparky.description


class OldStyleClass:
    "An old style class"
    # Original class style have been phased out in Python 3.

class NewStyleClass(object):
    "A new style class"
    # Introduced in Python 2.2
    #
    # Aside from this set of tests, Python Koans sticks exclusively to this
    # kind of class
    pass

print dir(OldStyleClass)
print len(dir(OldStyleClass))
print dir(OldStyleClass)
print str(OldStyleClass)
print repr(OldStyleClass)
print OldStyleClass.__module__
print OldStyleClass.__doc__

print type(OldStyleClass)

old_style = OldStyleClass()
print old_style.__class__

print "\n\n"


print dir(NewStyleClass)
print len(dir(NewStyleClass))
print dir(NewStyleClass)
print str(NewStyleClass)
print repr(NewStyleClass)
print NewStyleClass.__module__
print NewStyleClass.__doc__

print type(NewStyleClass)
print type(NewStyleClass) == NewStyleClass.__class__

new_style = NewStyleClass()
print type(new_style).__name__
print type(new_style)
print new_style.__class__

