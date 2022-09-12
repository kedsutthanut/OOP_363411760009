from MyPet import MyPet


# ใช้เเสดงตัวเลือกให้ผู้ใช้
"""
1.เพิ่มข้อมูลสัตว์เลี้ยง
2.เเสดงข้อมูลสัตว์เลี้ยง
3.ออกจากระบบ
"""
def display_option():
    print("\---Welcom, to Pet data store system---")
    print("1. add pet data.")
    print("2. display pets data.")
    print("3. exit.")

    select = int(input("select(1-3)? :"))
    if select ==1:
        input_mypet_data()
    elif select ==2:
        display_MyPet()
    elif select ==3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, enter 1-3 only. Thank.\n")

# ใช้เเสดงข้อมูลสัตวเลี้ยง์ทั้งหมด
def display_MyPet():
    if len(mypet_list) ==0:
        print(f"You had no pet data.")
    else:
        print(f"Your had {len(mypet_list)} foollowing:")
    for x in mypet_list:
        x.display_info()

# ใช้รับข้อมูลสัตว์เลี้ยงทั้งหมด
def input_mypet_data():
    name = input("Enter your pet name:")
    age = input("Enter your pet age:")
    breed = input("Enter your pet breed:")

    mypet_list.append(MyPet(name,age,breed))


# list
mypet_list = []
s=0
while s == 0:
    display_option()



















