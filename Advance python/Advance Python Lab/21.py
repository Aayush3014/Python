'''21. Write a program to create an abstract class Vehicle.
Derive three classes Car, Motorcycle and Truck from it.
Define appropriate methods and print the details of vehicle'''

class Vehicle:
    def vehicle_number(self):
        raise NotImplementedError()
    def fuel_type(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
    def no_of_wheels(self):
        raise NotImplementedError()
    def cc(self):
        raise NotImplementedError()        

class Car(Vehicle):
    def vehicle_number(self):
        return "BP08-5200"
    def fuel_type(self):
        return "Diesel"
    def color(self):
        return "Black"
    def no_of_wheels(self):
        return "Four"
    def cc(self):
        return "1690cc"


class Motorcycle(Vehicle):
    def vehicle_number(self):
        return "BR06-0420"
    def fuel_type(self):
        return "Petrol"
    def color(self):
        return "white"
    def no_of_wheels(self):
        return "Two"
    def cc(self):
        return "360cc"


class Truck(Vehicle):
    def vehicle_number(self):
        return "BR06-2569"
    def fuel_type(self):
        return "Diesel"
    def color(self):
        return "Orange"
    def no_of_wheels(self):
        return "Tweleve"
    def cc(self):
        return "5005cc"

Jaguar=Car()
print("Car--------->>",Jaguar.vehicle_number(),Jaguar.fuel_type(),Jaguar.color(),Jaguar.no_of_wheels(),Jaguar.cc())
print()
Bullet=Motorcycle()
print("Motorcycle-->>",Bullet.vehicle_number(),Bullet.fuel_type(),Bullet.color(),Bullet.no_of_wheels(),Bullet.cc())
print()
Turbo=Truck()
print("Truck------->>",Turbo.vehicle_number(),Turbo.fuel_type(),Turbo.color(),Turbo.no_of_wheels(),Turbo.cc())