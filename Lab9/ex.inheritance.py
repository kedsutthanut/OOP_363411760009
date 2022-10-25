"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""

# class relation - inhertance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')

class Student(Person): # student inherited from Person
    def __init__(self,name,age,major,gpa):
        # 1
        Person.__init__(self,name,age)
        self.major = major
        self.gpa = gpa
    def student_info(self):
        print(f'Name: {self.name} Age: {self.age}'f'Major: {self.major}'f'GPA: {self.gpa}')

# cerate object
s1 = Student("Sutthanut Yangrit",21,"MIT",3.00)
s1.person_info()
s1.student_info()