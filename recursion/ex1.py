class Fibo(object):
    def __init__(self):
        print "I have been created"

    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    def whatAmI(self, passMyInstance):
        print(self == passMyInstance)


