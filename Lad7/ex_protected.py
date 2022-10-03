"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""

class Persan:
    def __init__(self,id,name):
        self.__id = id # private memher
        self.__name = name
        self.__natian = "Thai" # protected member
    # gastter and setter mether
    def get_id(self):
        return self.__id
    def get_name(self):
        return  self.__name
    def set_name(self,name):
        self.__name =name
    def person_info(self):
        print(f'I am Person ID:'f'Name:{self.__name}' f'Nation:{self.__nation}')

class Student(Person):
    def __init__(self,id,name,uni):
        self.uni =uni
        Person.__init__(self,id,name)
    def student_info(self):
        print(f'I am student, ID:{self.__id()}'
            f'Name:{self.__name()}'
            f'Nation:{self.__nation()}'
            f'University: {self.uni}')




# create object
std = Student("009","sutthanut Yangrit")
print(std.get_id())
print(std.get_name())

p = Parson("009","sutthanut Yangrit")
print(p.get_id())
print(p.get_name())

std.student_info()
p.person_info