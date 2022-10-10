"""
Name: {Sutthanut Yangrit}
SID: {363411760009}
Group: {MIT431}
"""
"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""


class Vehicle :
    def __init__(self, brand, model, color,maxspeed,price):
        self.__brand = brand
        self.__model = model
        self.__colar = color
        self.__maxspeed = maxspeed
        self.__price = price

    def get__brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand
    def get__model(self):
        return  self.__model
    def set_model(self,model):
        self.__model = model
    def get__colar(self):
        return  self.__colar
    def set_colcr(self,colcr):
        self.__colcr = colcr
    def get__maxspeed(self):
        return self.__maxspeed
    def set_maxspeed(self, maxspeed):
        self.__maxspeed = maxspeed
    def get__price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price
    def display_Vehicle(self):
        print(f'Person brand:{self.__brand}' f'model:{self.__model}'f'colcr:{self.__colcr}'f'maxspeed:{self.__maxspeed}'f'price:{self.__price}')

    brand = input('Enter your ยี่ห้อรถ (brand) : ')
    model = input('Enter your รุ่นรถ (model) : ')
    color = input('Enter your สีรถ (color) : ')
    maxspeed = input('Enter your ความเร็วสูงสุด (max speed) : ')
    price = input('Enter your ราคา (price) : ')
    print('ยี่ห้อรถ :', brand)
    print('รุ่นรถ :', model)
    print('สีรถ :', color)
    print('ความเร็วสูงสุด :', maxspeed, 'กิโลเมตร')
    print('ราคา :', price, 'บาท')