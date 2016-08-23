
# Generator method (uses yield)
def list_of_items():
    yield 'peanut'
    yield 'butter'
    yield 'jelly'
    yield 'time'

for item in list_of_items():
    print item

for item in list_of_items():
    print next(list_of_items())


gen = (item * 2 for item in range(5))
comprehension = [item * 2 for item in range(5)]

print str(gen)
print str(comprehension)

# Generator is an object, not a list:
for item in gen:
    print item

# Can't iterate through generator more than once:
for item in gen:
    print item



def cubes(items):
    for item in items:
        yield item * item * item

def addTen(collection):
    for item in collection:
        yield item + 10


newList = addTen(range(2, 15))
print list(newList)

cube = cubes(range(2, 5))

print list(cube)


def accepter():
    item = yield
    print str(item)
    yield item

    item = yield
    print str(item)
    yield item


acc = accepter()
next(acc)
acc.send("hello")
next(acc)
acc.send("1")


