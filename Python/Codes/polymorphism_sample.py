class Parent(object):
    def method_a(self):
        print ("invoking PARENT method_a!")


class Child(Parent):
    def method_a(self):
        print ("invoking CHILD  method_a")


dad = Parent()
son = Child()


dad.method_a()
son.method_a()

# As you can see, when we invoke dad.method_a() it
# runs the Parent.method_a function because that variable (dad) is a Parent.
# However, when we invoke son.method_a() it prints out the Child.method_a messages
# because the son is an instance of Child and Child overrides that function by defining its own version.

# Polymorphism
# Polymorphic behavior allows you to specify common methods in an "abstract" level and
# implement them in particular instances. It is the process of using an operator or function
# in different ways for different data input.


class Person(object):
  def pay_bill(self):
      print ("I am a person")


# Millionaire inherits from Person
class Millionaire(Person):
  def pay_bill(self):
      print ("Here you go! Keep the change!")


# Grad Student also inherits from the Person class
class GradStudent(Person):
  def pay_bill(self):
      print ("Can I owe you ten bucks or do the dishes?")

person_1 = GradStudent()
print (person_1.pay_bill())

# Based on this example, a Millionaire and a Grad Student are both Persons.
# However, when it comes to paying a bill, how they act is quite different.
# This pattern is useful when you know that each subclass of a parent class must define a
# specific behavior in a method, and you don't want to define a default behavior
# in the parent class (hence the pure virtual implementation in the parent).

