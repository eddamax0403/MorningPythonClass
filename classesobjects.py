class Student:
    #Proprties/Variables/Characteristics/Attributes
    name = "Tess"
    gender = "Female"
    age = 21

    #Behaviour/Method
    def study(self):
        print("Student is studying")

mystudent = Student() #This is creating an object
mystudent.study()

print(mystudent.name)
print(mystudent.gender)
print(mystudent.age)