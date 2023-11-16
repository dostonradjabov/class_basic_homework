class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

from create_two_attribute_one_objects import Person

person = Person(name = "Ali", age = 25)

print("Name:",person.name)
print("Age:",person.age)