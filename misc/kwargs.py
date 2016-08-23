# Variable length keyword arguments in python:

def proxy(func, *args, **kwargs):
    print str(func)
    print str(args)
    print str(kwargs)

    for key, value in kwargs.iteritems():
        print key, ": ", value

proxy( lambda(x): x*x, "one", "two" )
proxy( lambda(x): x*x, one="uno", two="zwei" )
proxy( lambda(x): x*x, "ein", "zwei", one="uno", two="zwei" )

