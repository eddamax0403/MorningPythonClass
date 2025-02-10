class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def details(self):
        print(self.name,"is a",self.gender,"at",self.age)


teacher = Person("Joe","Male",45)
teacher.details()
print(teacher.name)

accountant = Person("Mary","Female",27)
accountant.details()
print(accountant.name)
