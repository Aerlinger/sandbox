class Dog:
    #@class_method
    def class_method(cls):
        return "A class method"

    # Knows nothing about the class it was called on and does not require access to the class
    #@static_method
    def static_method():
        return "A static method"


    class_method = classmethod(class_method)
    static_method = staticmethod(static_method)


print Dog.class_method()
print Dog.static_method()

fido = Dog()
# Static and class methods can be called on instances or classes:
print fido.static_method()
print fido.class_method()
