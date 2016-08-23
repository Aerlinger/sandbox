import re

# An abstract class:
class Node(object):

    def execute(self):
        pass


class Number(Node):

    def __init__(self, value):
        self._value = value

    def execute(self):
        return self._value


class Operator(Node):

    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def execute(self):
        pass


class Add(Operator):

    def execute(self):
        return self.left.execute() + self.right.execute()


class Subtract(Operator):

    def execute(self):
        return self.left.execute() - self.right.execute()


class Divide(Operator):

    def execute(self):
        return self.left.execute() / self.right.execute()


class Multiply(Operator):

    def execute(self):
        return self.left.execute() * self.right.execute()


One     = Number(1)
Two     = Number(2)
Three   = Number(3)
Four    = Number(4)
Five    = Number(5)
Six     = Number(6)
Seven   = Number(7)
Eight   = Number(8)
Nine    = Number(9)


root = Add()

sub = Subtract(Five, Three)
mult = Multiply(Nine, Eight)

root.right = sub
root.left = mult

print root.execute()



# Next create a parser to parse an expression such as:

# Example: [1/5 + 5 + 9*3 - 1]

# Solution Build a tokenizer:

equation = "1/5 + 5 + 9*3 - 1"

scores = { '/': 1,
           '*': 1,
           '+': 2,
           '-': 2 }

# Strip whitespace:

equation = ""

tokens = {}
terminals = {}
parsed = {}