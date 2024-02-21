class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance():
            return self.value == other.value
        return False

# Create some instances of MyClass
obj1 = MyClass(1)
obj2 = MyClass(2)
obj3 = MyClass(3)

# Create obj4 with the same value as obj2
obj4 = MyClass(5)

# Create a list of objects
object_list = [obj1, obj2, obj3]

# Check if obj4 is in the list using the 'in' keyword
if obj4 in object_list:
    print("obj4 is in the list")
else:
    print("obj4 is not in the list")

# Check if any object in the list has the same value as obj4 using 'any()'
if any(obj == obj4 for obj in object_list):
    print("At least one object with the same value as obj4 is in the list")
else:
    print("No object with the same value as obj4 in the list")