#Create a "Person" class

#that has a name("name") and a age("age")
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person(name = "Ali", age = 25)

print("Name:", person.name)
print("Age:", person.age)