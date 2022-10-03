"""
Name: {Sutthanut Yangrit}
SID  : {363411760009}
Group : {MIT431}
"""

class Labtop:

    def __init__(self,no,brand,model,cpu,ram,display,storage,price):
    # opject attribute
        self.no = no
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram =ram
        self.display = display
        self.storage = storage
        self.price = price
    def display_labtop(self):
        print(f'no: {self.no} brand: {self.brand} model: {self.model} cpu: {self.cpu} ram: {self.ram} display: {self.display} storage: {self.storage} price: {self.price}')


