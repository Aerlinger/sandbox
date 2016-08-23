# A decorator can be declared as an object
# takes a name in the `@syntax`.
#
# The decoarted method is implicitly passed as an argument to the __call__ method
# the *args splat
#
# @splitter(10)
# def wrapped_fun("my args")
#   return "lol"
# end
#
class splitter(object):
    def __init__(self, packet_size):
        print "Initializing spliter decorator..."
        print "Number of iterations:", str(packet_size)
        self.packet_size = packet_size


    def __call__(self, fn):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        print "Inside __call__()"
        def wrapped_f(*args):
            items = args[0]
            num_packets = int(len(items)/self.packet_size)

            print "\tInside wrapped_f()"
            print "\tIterating", self.packet_size, "times"

            for index in range(num_packets):
                fn(items[index*self.packet_size:(index+1)*self.packet_size])

            print "\tAfter f(*args)"
        return wrapped_f
