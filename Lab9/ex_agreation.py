"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""
# class relation - agreation

class Teacher:
    def __init__(self,name):
        self.name = name
    def teacher_info(self):
        print(f'Teacher Name; {self.name}')


class Faculty:
    lst_teacher = list()
    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'Faculty Name: {self.fac_name} ')
    def add_teacher(self,Teacher):
        self.lst_teacher.append(Teacher)
    def teacher_info(self):
        print(f'In {self.fac_name} has teacher beloe:')
        for x in  self.lst_teacher:
            x.teacher_info()


f1 = Faculty("MT")

t1 = Teacher("Sutthanut")
t2 = Teacher("Nattamon")

f1.add_teacher(t1)
f1.add_teacher(t2)
# display data
t1.teacher_info()
t2.teacher_info()

f1.fac_info()
f1.teacher_info()