"""
Name: {Sutthanut Yangrit}
SID: {363411760009}
Group: {MIT431}
"""

# create class
class Student:
    # class Attribute
    University = "RUTS"
    def __init__(self,name,major):
        # object attributes
        self.name = name
        self.major = major

# create object
s1 = Student("Nattakamon Jitjamnong","MIT")
s2 = Student("Sutthanut Yangrit","MIT")
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