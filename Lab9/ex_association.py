"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""

class Student:
    lst_Student = list()
    def __init__(self,name,age,major,gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def student_info(self):
        print(f'Name: {self.name} Age: {self.age}'f'Major: {self.major}'f'GPA: {self.gpa}')



    def add_advisor(self,Teacher):
        self.lst_Student.append(Teacher)
    def advisor_info(self):
        print(f'My Teacher follwing:')
        for x in self.lst_Student:
            print(f'\t {x.name}')

class Teacher:
    lst_student = list()
    def __init__(self,name):
        self.name = name
    def teacher_info(self):
        print(f'Name; {self.name}')

    def add_student(self,Student):
        self.lst_student.append(Student)

    def student_info(self):
        print("My students following: ")
        for x in self.lst_student:
            print(f'\t {x.student_info}')

# create object
s1 = Student("Sutthanut Yangrit",21,"MIT",3.00)
s2 = Student("Parichat Sakkuna",25,"MIT",3.50)

t1 = Teacher("Marisa")
t2 = Teacher("Suttanut")

# association
s1.add_advisor(t1)
s1.add_advisor(t2)
s1.student_info()
s1.advisor_info()


t1.add_student(s1)
t1.add_student(s2)
t1.teacher_info()
t1.student_info()
