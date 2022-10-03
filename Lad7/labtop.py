"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""
class Labtop:
    def __init__(self,brand,model,cpu,ram,display,storage,price):
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage =storage
        self.__price = price

    def get__brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand
    def get__model(self):
        return  self.__model
    def set_model(self,model):
        self.__model = model
    def get__cpu(self):
        return  self.__cpu
    def set_cpu(self,cpu):
        self.__cpu = cpu
    def get__ram(self):
        return  self.__ram
    def set_ram(self,ram):
        self.__ram = ram
    def get__display(self):
        return self.__display
    def set_display(self,display):
        self.__display = display
    def get__storage(self):
        return self.__storage
    def set_storage(self,storage):
        self.__storage = storage
    def get__price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price
    def display_labtop(self):
        print(f'Person brand:{self.__brand}' f'model:{self.__model}'f'cpu:{self.__cpu}'f'ram:{self.__ram}'f'display: {self.__display}'f'storage:{self.__storage}'f'price:{self.__price}')

