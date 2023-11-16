#Create a "Person" class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

person = Person(name="John", age=30)


print("Name:", person.get_name())
print("Age:", person.get_age())


person.set_name("Alice")
person.set_age(25)


print("Modified Name:", person.get_name())
print("Modified Age:", person.get_age())