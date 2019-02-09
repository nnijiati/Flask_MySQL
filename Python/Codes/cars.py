class Vehicle:
    def __init__(self, wheels, make, model):
        self.wheels = wheels
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self,miles):
        self.mileage += miles
        return self

    def reverse(self,miles):
        self.mileage -= miles
        return self


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"


class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self.wheels

v = Vehicle(4,"dodge","minivan")
print (v.make)

b = Bike(2,"Schwinn","Paramount")
print (b.vehicle_type())

c = Car(2, "toyota", "4Runner")
print (c.set_wheels())


# class Parent(object): # inherits from the object class
#   # parent methods and attributes here
# class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
#   # parent methods and attributes are implicitly inherited
#   # child methods and attributes
#  lalala