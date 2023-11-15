#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person:
    def __init__(self,name):
        self.name = name

person1 = Person("John Doe")
print(person1.name)