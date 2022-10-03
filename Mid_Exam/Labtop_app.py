from Labtop import Labtop

"""
1.เพิ่มข้อมูล Labtop
2.เเสดงข้อมูล Labtop
3.ออกจากระบบ
"""
def display_option_system():
    print("\n---Welcome, to labtop data store system---")
    print("1. add labtop data.")
    print("2. display labtop data.")
    print("3. exit.")

    select = int(input("select(1-3)? :"))
    if select ==1:
        input_laptop_data()
    elif select ==2:
        display_labtop()
    elif select ==3:
        print("Log out successfully.")
        exit(0)
    else:
        print("Please, enter 1-3 only. Thank.\n")


def display_laptop():
    if len(Labtop_list) ==0:
        print("You had no labtop data.")
    else:
        print(f"You had {len(labtop_list)} following:")
    for x in labtop_list:
        x.display_info()

def input_laptop_data():
        no = input("Enter your laptop no:")
        brand = input("Enter your laptop brand:")
        model = input("Enter your laptop model:")
        cpu = input("Enter your laptop cpu:")
        ram = input("Enter your laptop ram:")
        display = input("Enter your laptop display:")
        storage = input("Enter your laptop storage:")
        price = input("Enter your laptop price:")

        labtop_list.append(Labtop(no,brand,model,cpu,ram,display,storage,price))

Labtop_list = []
s = 0
while s == 0:
     display_option_system()