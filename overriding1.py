# Python program to demonstrate method overriding
# Defining parent class
class Parent:
    # Parent's show method
    def show(self):
        print("We are in base class")

# Defining child class
class Child(Parent):
    # Child's show method
    def show(self):
        print("We are in derived class")

# Driver's code
obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()
