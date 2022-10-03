from labtop import Labtop

#display
def display_labtop():
    if len (my_labtop) ==0:
        print("\nyou had no labtop data:\n")
    else:
        num = 1
        print(f'You had {len(my_labtop)}following:')
        for x in my_labtop:
            print(f'{num}. ',end="")
            x.display_labtop()
            num +=1
        print("\n")

# opion
def display_option_system():
    print("Welcome, to labtop data store system---")
    print("1. add labtop data.")
    print("2. display labtop data.")
    print("3. Delete labtop.")
    print("4. Edit ladtop price")
    print("5. exit.")
    select = int(input("select(1-5)? :"))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        delete_labtop()
    elif select == 4:
        edit_labtop_rice()
    elif select == 5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-5.")
# edit_data
def edit_labtop_rice():
    def delete_labtop():
        display_labtop()
        # lebget of my_labtop
        n = len(my_labtop)
        s = int(input(f"select 1-{n} or type 0 to main option : "))
        while s:
            s = int(input(f"select 1{n} or type 0 to main option: "))
            if s in range(1, n + 1):
                print(f'current price:{my_labtop[s-1].get__price()}')
                newppice = float(input("enter new price: "))
                my_labtop[s-1].set_price(newppice)
                print("\nAlready deleted labtop data.\n")
                break
            elif s == 0:
                break
            else:
                print(f"Please,enter number 1-{n} or type 0 to main option: .")


# delete data
def delete_labtop():
    display_labtop()
    # lebget of my_labtop
    n = len(my_labtop)
    s = int(input(f"select 1-{n} or type 0 to main option : "))
    while s:
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("Already deleted labtop data.")
            break
        elif s == 0:
            break
        else:
            print(f"Please,enter number 1-{n}.")


# input data
def input_laptop_data():
    brand = input("Enter your laptop brand:")
    model = input("Enter your laptop model:")
    cpu = input("Enter your laptop cpu:")
    ram = int(input("Enter your laptop ram:"))
    display = float(input("Enter your laptop display:"))
    storage = int(input("Enter your laptop storage:"))
    price = float(input("Enter your laptop price:"))

    #return brand,model,color,maxspeed,price # return as tuple
    my_labtop.append(Labtop(brand,model,cpu,ram,display,storage,price))
    print("\n------------------------------------")
    print("Already add Labtop to store.")
    print("\n------------------------------------")

my_labtop = []
my_labtop.append(Labtop("ASUS","Vivvobook","Intel Core i5-12500H",8,15.6,512,27990))
my_labtop.append(Labtop("Lennovo","IdeaPad Gaming 3","Intel Core i5-11320H",8,15.6,512,25990))

s = 0
while s ==0:
    display_option_system()

