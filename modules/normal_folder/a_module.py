
inNormalNamespace = "normal_folder"

class NormalFolder1:

    def __init__(self, name, type = "Class"):
        self.myName = name
        self.type = type

    def getMyName(self):
        print self.myName
        return self.myName


class NormalFolder2:

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz


    def foo(self):
        return self.foo

    def bar(self):
        return self.bar

    def baz(self):
        return self.baz