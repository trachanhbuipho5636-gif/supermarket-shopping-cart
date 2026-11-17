cart = []
food = ["pizza", "hamburger", "apple", "milk", "apple_pie", "ice_cream", "sugar_cane"]
food_price = [1.50, 3.99, 0.79, 2.99, 7.50, 0.50, 0.10]
total_price = 0

command_list = ["remove", "add", "user", "staff", "q"]
command_help = ["remove   (Choose when you want to remove a product - only for staff)",
                "add      (Choose when you want to add a product - only for staff)",
                "user     (Choose if you are a normal user)",
                "staff    (Choose if you are a staff",
                "q        (Choose if you want to quit"]

product_quantity = 7

cnt = 0
flag = False

intro = input("Enter user or staff to continue (q to quit): ")

def print_help():
    print('\n')
    for i in range(5):
        print(command_help[i])
    print('\n')

def print_your_cart():
    global cnt

    print('\n')
    print("------------------")
    if cnt == 0:
        print("Your cart is empty")

    else:
        for i in range(cnt):
            id = food.index(cart[i])
            print(cart[i], " ", f"${food_price[id]:.2f}")
    print("------------------")
    print('\n')


def print_bill():
    print('\n')
    print("----------Your Bill---------")
    print(f"You bought : {cnt} product(s)", '\n')
    for i in range(cnt):
        id = food.index(cart[i])
        print(cart[i], ' ', f"${food_price[id]:.2f}")
    print('\n')
    print("--------Payment Details------")
    print(f"You must pay : ${total_price:.2f}")
    print("-----------------------------")
    print('\n')

def print_food_list():
    global product_quantity

    print('\n')
    print("------Food list------")
    for i in range(product_quantity):
        print(food[i], " : ", f"${food_price[i]}")
    print("---------------------")
    print('\n')

def customers() :
    global cnt
    global total_price
    global flag
    global product_quantity

    command = input("Enter what do you want(q to quit): ")

    if command == "remove":
        name = input("Enter product name to remove: ")

        while name not in cart:
            print("This product is not in the food list")
            name = input("Enter product name to remove: ")
        cart.remove(name)
        cnt -= 1
        id = food.index(name)
        total_price -= food_price[id]


    else:
        while (command not in food) and (command != "q"):
            print(f"{command} is not in the food list")
            print("Please enter the correct product name", '\n')
            command = input("Enter what do you want(q to quit): ")

        if command == "q":
            flag = True
            print_bill()
            return

        else:
            cart.append(command)
            cnt += 1
            id = food.index(command)
            total_price += food_price[id]

    print_your_cart()

def staff() :
    global product_quantity
    global intro

    command = input("Do you want to remove or add a product? (q to quit) (remove/add) : ")

    if command not in command_list:
        print("Please enter the correct command or use --help to see available commands",'\n')
        print('\n')

    if command == "--help":
        print("Available commands:",'\n')
        for i in range(5):
            print(command_help[i])

    elif command != "q":
        if command == "add":
            name = input("Enter product name to add: ")
            price = float(input("Enter the product price: "))
            food.append(name)
            food_price.append(price)
            product_quantity += 1
            print_food_list()

        if command == "remove":
            name = input("Enter product name to remove: ")
            while name not in food:
                print("This product is not in the food list")
                name = input("Enter product name to remove: ")
            else:
                id = food.index(name)
                food.remove(name)
                food_price.remove(food_price[id])
                product_quantity -= 1
                print_food_list()
    else:
        intro = ""

while True:

    if intro == "--help":
        print_help()
        intro = input("Enter user or staff to continue (q to quit): ")
        continue

    if intro == "":
        intro = input("Enter user or staff to continue (q to quit): ")
        continue

    if intro not in command_list:
        print("Please enter the correct command or use --help to see available commands",'\n')
        intro = input("Enter user or staff to continue (q to quit): ")
        continue

    if intro == "q":
        break

    if intro == "staff":
        staff()

    if intro == "user":
        customers()
        if flag == True:
            break

    if intro == "remove" or intro == "add":
        print("You do not have enough permission to do that")
        intro = input("Enter user or staff to continue (q to quit): ")