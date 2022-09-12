"""
Name: {Sutthanut Yangrit}
SID: {363411760009}
Group: {MIT431}
"""

class MyPet:
    # class attribute
    MyPet =[]
    def __init__(self,name,age,breed):
     # class attribute
        self.name = name
        self.age = age
        self.breed = breed
        self.MyPet.append(self)

def display_info(self):
    print(f'name: {self.name} Age: {self.age} Breed: {self.breed}')







