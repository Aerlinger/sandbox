

class Hooks(object):

    def __init__(self, name='HooksClass', *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.i = 0

        print "initialized %s with arguments %s and keyword args: %s" % (self.__class__, args, kwargs)

    def __call__(self, *args, **kwargs):
        print "\tCALL: %s with arguments %s and keyword args: %s" % (self.__class__, args, kwargs)


    def __del__(self):
        print "DELETING: %s" % (self.name)

    def __delete__(self, instance):
        print "Deleting: %s" % instance


    def __iter__(self):
        return iter(self.args)

    def __len__(self):
        return len(self.args)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Exited %s, %s, %s" % (exc_type, exc_val, exc_tb)


    def __abs__(self):
        return self.name.upper()

    def __str__(self):
        return "I AM %s" % self.name

    def __int__(self):
        return len(self.kwargs)

    def __index__(self):
        return self.i + 1

#    def __complex__(self):
#        return "I AM COMPLEX AND SEXY i"



hooks = Hooks()
Hooks()

print str(hooks)

hooks = Hooks(1, 2, 3, "four", "cinco")

print "Length of hooks: %s" % len(hooks)
for item in hooks:
    print item

hooks = Hooks(ein=1, zwei=2, drei=3)
print "Length of kwargs: %s" % int(hooks)

hooks = Hooks('one', 'two', 'three', ein=1, zwei=2, drei="tres")

del hooks