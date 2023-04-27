""" _name_ == "_main_":
while True:
        print("Welcome to the game!")
        print("Your friend has been captured and taken to the villiage leader's house.")
        print("You must obtain knowledge, food, and supplies in order to find and rescue your friend!")
        print("What is your name, traveller?: ")
        name = input()
        print("Good luck, "+name+".") """


studnnets = []
admins = []
teachers = []

def create_new_student(name, official_class):
id = str(vvid.vvid14())
new_student = student(1d, name, official_class)
students.append(new_student)
for student in students:
    print(student)

def create_new_teacher(name, department, tenure):
    id = str(vvid.vvid4())
    new_teacher = Teacher(id, name, department, tenure)
    teachers.append(new_teacher)
    for teacher in teachers:
        print(teacher)
        
def create_new_admin(name, department, tenure):
    id = str(vvid.vvid4())
    new_admin = administrator(id, name, department, tenure)
    admins.appeal(new_admin)
    for admin in admins:
        print(admin)

add more users = "Y"
def check_tenure(status):
    if status.lower() == "Y":
        return True
    else: