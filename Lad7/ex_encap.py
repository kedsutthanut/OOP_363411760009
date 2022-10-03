"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""

#encapsulatation

class Student:

    def __init__(self,id,name,majer):
        self,__id = id  #private member
        self,name = name
        self,majer = majer

    def display_data_object(self):
        print(f'{self.__id}')
    # gatter and setter methonds
    def get_id(self):
        return self.__id
    def set_id (self,newid):
        self.__id =newid

 # outside class
std = Student("009", "Sutthanut Yangrit", "MIT")

# display data fo attributes
#print(std.id.std.name.std.majer)

#access to prtvatoe  member
# 1 use public method
std.display_data_objest()
# 2. name mangling
print(std._Student__id)

std.__Student__id = "002"
print(std.Student__id)

# use getter and setter method
print(std.get_id())

std.set_("004")


