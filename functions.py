#Built-in functions

y = max(56,75,23,18,94,48)
print("The maximum value is",y)

x = min(24,7,76,97,16)
print("The minimum value is",x)

#User-defined functions
def name():
    print("Eddie")
name() #This is calling a function

def product():
    a = 20
    b = 10
    print(a*b)
product()

#Parameters/variable and arguments/value
def sum(num1,num2):
    print(num1+num2)
sum(5,6)
sum(10,40)
sum(70,67)


def employee(name,age,position,salary):
    print(name,age,position,salary)

employee("Eddie",24,"CEO",860000.00)
employee("John",20,"Manager",500000.00)

#Program to display details of 5 students
#fullname,age,course,gender,nationality

def student(Fullname,Age,Course,Gender,Nationality):
    print(Fullname,Age,Course,Gender,Nationality)
student("Alex Kiraithe",18,"MIT","Male","Kenyan")
student("Monica Green",20,"Cyber Security","Female","Canadian")
student("Yusuf Mohammed",22,"Data Science","Male","Turkish")
student("Ibrahim Djokovic",19,"MIT","Male","Croatian")
student("Zubeida Hassan",21,"Data Science","Female","Tanzanian")





