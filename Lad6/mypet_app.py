from ex_clss2 import Mypet
def input_pet_data():
    name = input("Enter your pet name:")
    age = int(input("Enter your pet age:"))
    breed = input("Enter your pet breed:")

    return name,age,breed
data = input_pet_data()
p1 = Mypet(data[0],data[1],data[2])
p1.display_info()

data = input_pet_data()
p2 = Mypet(data[0],data[1],data[2])
p2.display_info()
print(f"")