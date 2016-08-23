import "../decorators"

@doubler
def echo(saying):
    return saying

print doubler(echo)

def echo2(saying):
    return saying



print echo("hello")
print echo("hey")

d = doubler(echo2)
print d("Yo")

d = doubler(echo)
print d("Yo")



class documenter(object):
    def __init__(self, *args):
        self.doc = args[0]
        print "Created a documenter with args: ", str(args[0])

    def __call__(self, func, *args):

        print "Called!", args

        if func.__doc__:
            func.__doc__ += self.doc
        else:
            func.__doc__ = self.doc

        return func

@documenter("this function sucks")
def some_function(*args):
    return args

some_function("blah")
some_function("blah")
print some_function.__doc__
