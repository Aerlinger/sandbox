class doubler(object):
    def __init__(self, fn):
        print "Defined doubler with" + str(fn)
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print "calling with " + str(args)
        return self.fn(*args) + ", " + self.fn(*args)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Exiting..."