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


print dir(Fibo)
ding = Fibo()
newObj = ding.__init__()
print dir(ding)

print ding.fib(5)
ding.whatAmI(ding)

class Nietschze:
    def lament(self):
        self.whoAmI(self)

    def whoAmI(self, myself):
        print "I am myself " + str(self == myself)


nietschze = Nietschze()
nietschze.lament();
