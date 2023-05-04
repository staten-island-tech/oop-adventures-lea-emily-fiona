""" _name_ == "_main_":
while True:
        print("Welcome to the game!")
        print("Your friend has been captured and taken to the villiage leader's house.")
        print("You must obtain knowledge, food, and supplies in order to find and rescue your friend!")
        print("What is your name, traveller?: ")
        name = input()
        print("Good luck, "+name+".") """

import uuid

class User:
    def _init_(self, id, name):
        self.id = id
        self.name = name 
new_id = str(uuid.uuid4())
mark = User(new_id, "Mark")
print(mark.id, mark.name)

""" class Student(User):
    def _init_(self, id, name, official_class):
        super()._init_(id, name)
        self.official_class = official_class
    def _str_(self):
        return f"{self.name}, {self.id}"
    
class Teacher(User):
    def _init_(self, id, nme, department, tenure):
        super()._init_(id, name)
        self.privileges = "teacher"
        self.department = department
        self.tenure = tenure
    def _str_(self):
        return f"{self.name}, {self.department}, tenure = {self.tenure}"
    
class Administrator(Teacher):
    def _init_(self, id, name, department, tenure):
        super()._init_(id, name, department, tenure)
        self.privileges = "Admin"
    def _str_(self):
        return f"{self.name}, {self_id}, {self.department}, tenure = {self.tenure}"
students = []
admins = []
teachers = []

def create_new_student(name, official_class):
    id = str(uuid.uuid14())
new_student = student(id, name, official_class)
students.append(new_student)
for student in students:
    print(student)

def create_new_teacher(name, department, tenure):
    id = str(uuid.uuid4())
    new_teacher = Teacher(id, name, department, tenure)
    teachers.append(new_teacher)
    for teacher in teachers:
        print(teacher)
        
def create_new_admin(name, department, tenure):
    id = str(uuid.uuid4())
    new_admin = administrator(id, name, department, tenure)
    admins.appeal(new_admin)
    for admin in admins:
        print(admin)

add more users = "Y"
def check_tenure(status):
    if status.lower() == "Y":
        return True
    else:
        return False
while add more users == "Y":
user_request = input("What type of user are you adding?")
if user_request.upper()== "STUDENT":
    name = input("Enter user name")
    official_class = input("Enter official class: ")
    create_new_student(name, official_class)
elif user_request.upper() == "TEACHER":
    name = imput("Enter user name")
    department = input("Enter department name: ")
    tenure_query = input(Do they have a tenure Y/N: )
    tenure = check_tenure(tenure_query)
    create_new_teacher(name, department, tenure)
elif user_request.upper() == "ADMIN":
    name = imput("Enter user name")
    department = input("Enter department name: ")
    tenure_query = input(Do they have a tenure Y/N: )
    tenure = check_tenure(tenure_query)
    create_new_teacher(name, department, tenure)

else:
    print("something went wrong, are you sure you typed the request correctly?")
still_continue = input("Would you like to continue Y/N").uppser()
add_more_users = still_continue """

""" class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age) """
""" 
class Person:
    def __init__(feature, eye, age):
        feature.eye = eye
        feature.age = age
    def __str__(feature):
        return f"{feature.eye}({feature.age})"
p1 = Person("green", 17)

print(p1)
 """

""" class Person:
    def __init__(feature, eye, age):
        feature.eye = eye
        feature.age = age
    
    def myfunc(abc):
        print("Hi, my eye color is " + abc.eye)
    
p1 = Person("green", 17)

del p1.age
print(p1.eye)
 """
""" class Person:
    def __init__(feature, eye, age):
        feature.eye = eye
        feature.age = age

    def printfeatures(feature):
        print(feature.eye, feature.age)



class Child(Person):
    def __init__(feature, eye, age, year):
       super().__init__(eye, age)
       feature.dob = year


    def stats(feature):
     print("Welcome your stats are", feature.eye, feature.age, "and your year is", feature.dob)

x = Child("brown", "26", 1999)
x.stats() """