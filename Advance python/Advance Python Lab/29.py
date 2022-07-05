'''29. Write a program to inspect the object using type() ,id(), isinstance(), issubclass()
and callable() built-in function.'''

# Defining the parent class


class Vehicles:
    # Constructor
    def __init__(self):
        pass

# Defining Child class


class Car(Vehicles):
    # Constructor
    def __init__(self):
        Vehicles.__init__(self)
        print("Inspecting the object..............")


C = Car()

# Inspecting the object using type()
print('Inspecting using type() ---->>> ', type(C))
# Inspecting the object using id()
print('Inspecting using id() ---->>> ', id(C))
# Inspecting the object using isinstance()
print('Inspecting using isinstance() ---->>> ', isinstance(C, Car))
# Inspecting the object using issubclass()
print('Inspecting using issubclass() ---->>> ', issubclass(Car, Vehicles))
# Inspecting the object using callable()
print('Inspecting using callable() ---->>> ', callable(C))