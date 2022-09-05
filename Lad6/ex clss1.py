"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""

# create class
class Student:
    # class Attribute
    University = "RUTS"
    mystudent =[] # list
    def __init__(self,name,major):
        # object attributes
        self.name = name
        self.major = major
        self.mystudent.append(self)

def __str__(selt):
    print(f'My mame is {selt.name},I am studenting in {selt.major}')
# create object
s1 = Student("Sutthanut Yangrit","MIT")
s2 = Student("Nattakamon Jitjamnong","MIT")
print(s1.name, s1.major)
print(s2.name, s2.major)
s1.major = "LM"
print(s1.name, s1.major)

# access to class attribute
print(s1.name, s1.University)
print(s2.name, s2.University)

s1.University = "Saiyai"
print(s1.name, s1.University)
print(s2.name, s2.University)
Student.University = "Thungsong"
print(s1.name, s1.University)
print(s2.name, s2.University)
print(len(Student.mystudent)

s1.__str__()
s2.__str__()
