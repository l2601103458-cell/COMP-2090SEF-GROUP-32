import os
import time
from customer import Customers
from restaurant import Restaurant


def login_function(file):
    acc_file = open(file, "r")
    acc_lines = acc_file.readlines()
    os.system("cls")
    print("Login")
    login = False

    while not login:
        print("(leave blank to go back)")
        print()
        username = input("Username: ")
        if username == "":
            os.system("cls")
            acc_file.close()
            break

        password = input("Password: ")
        if password == "":
            os.system("cls")
            acc_file.close()
            break

        for get_acc_data in acc_lines:
            acc_data = get_acc_data.strip().split(";")

            if username == acc_data[0] and password == acc_data[1]:
                login = True
                acc_file.close()
                global current_username, current_password, money
                current_username, current_password = username, password
                money = int(acc_data[2])
                return True
            
        os.system("cls")
        print("Wrong username or password. Please try again.")


def create_account():
    have_upper = False
    have_lower = False
    have_number = False
    create_pass = False
    os.system("cls")

    while not create_pass:

        print("Requirements of creating account:")
        print("1. Length of username should not excceed 12 characters")
        print("2. Length of password should be at least 8 characters")
        print("3. The password should consist of at least 1 uppercase letter, 1 lowercase letter and 1 number")
        print("4. No semicolon (;) is allowed for both username and password")
        print("(leave blank to go back)")
        print()

        new_username = input("Enter your username: ")
        if new_username == "":
            os.system("cls")
            break
        if len(new_username) > 12:
            os.system("cls")
            print("Requirement 1 not fulfilled. Please enter again.")
            continue
        if ";" in new_username:
            os.system("cls")
            print("Requirement 4 not fulfilled. Please enter again.")
            continue

        new_password = input("Enter your password: ")
        if new_password == "":
            os.system("cls")
            break

        if len(new_password) < 8:
            os.system("cls")
            print("Requirment 2 not fulfilled. Please enter again.")
            continue

        if ";" in new_password:
            os.system("cls")
            print("Requirement 4 not fulfilled. Please enter again.")
            continue

        for letters in new_password:
            if letters.isupper():
                have_upper = True
            if letters.islower():
                have_lower = True
            if letters.isdigit():
                have_number = True

        if have_upper and have_lower and have_number:
            Customers.create_acc(new_username, new_password)
            create_pass = True
            global current_username, current_password, money
            current_username, current_password = new_username, new_password
            money = 0
            return True
        else:
            os.system("cls")
            print("Requirement 3 not fulfilled. Please enter again.")
            continue

# ================================================================================ #

def refresh_money(username, password):
    acc_file = open("account.txt", "r")
    acc_lines = acc_file.readlines()

    for get_acc_data in acc_lines:
        acc_data = get_acc_data.strip().split(";")

        if username == acc_data[0] and password == acc_data[1]:
            money = int(acc_data[2])
            acc_file.close()
            return money
        else:
            word = "Error:account not found"
    return word

def get_restaurant_list(file):
    rest_list = []
    rest_file = open(file, "r")
    for rest_line in rest_file:
        rest_line = rest_line.strip()
        rest_name = rest_line.split(";")
        rest_list.append(rest_name[1])
    rest_file.close()
    return rest_list

def get_menu(rest_name):
    menu_list = {}
    rest_file_name = f"restaurant_data/{rest_name}_menu.txt"

    try:
        menu_file = open(rest_file_name, "r")
        for menu_line in menu_file:
            menu_line = menu_line.strip()
            menu_elements = menu_line.split(";")
            dish_type, dish_id, dish_name, price, sales = menu_elements
            dish_id = int(dish_id)
            price = int(price)
            sales = int(sales)

            dish_info = {
                "id" : dish_id,
                "name" : dish_name,
                "price" : price,
                "sales" : sales
            }

            if dish_type not in menu_list:
                menu_list[dish_type] = []
            menu_list[dish_type].append(dish_info)
        menu_file.close()
        return menu_list
    
    except FileNotFoundError:
        print("Error occured: restaurant menu not found.")
        return
    
def display_rest_menu(menu):
    for dish_type, dishes in menu.items():
        print(f"【{dish_type}】")
        for dish in dishes:
            print(f"    {dish['id']}. {dish['name']}\t${dish['price']}")
        print()

def food_ordering(selected_rest, username, password, money):
    no_of_dishes = 0
    order_wrong_input = False
    dish_choose_bool = False

    menu = get_menu(selected_rest)
    for dish_type in menu.values():
        for dish in dish_type:
            no_of_dishes += 1
            dish = dish     

    if not menu:
        print("This restaurant has no menu.")
        input("Press ENTER to continue...")
    else:
        while not dish_choose_bool:
            order_chosen = False
            os.system("cls")

            print(f"========== {selected_rest} ==========\n")
            display_rest_menu(menu)
            
            if order_wrong_input:
                print("Wrong input. Please enter again.")
                order_wrong_input = False

            print("(leave blank to go back)")
            dish_choose = input("Enter the corresponding number of dishes\n"
            "(you can choose more than one dish, separating with \",\"):\n")
            
            ordering_num = dish_choose.split(",")
            try:
                for i in range(len(ordering_num)):
                    ordering_num[i] = ordering_num[i].strip()
                    ordering_num[i] = int(ordering_num[i])
                    if ordering_num[i] <= 0 or ordering_num[i] > no_of_dishes:
                        order_chosen = False
                        order_wrong_input = True
                        break
                    else:
                        order_chosen = True
            except ValueError:
                order_wrong_input = True
            
            if order_chosen:
                os.system("cls")
                num_order = 1
                total_cost = 0
                ordered_dishes = []

                for dishes in menu.values():
                    for dish in dishes:
                        if dish['id'] in ordering_num:
                            total_cost += dish['price']
                            ordered_dishes.append(dish['name'])

                print("Your order:")
                for dishes in ordered_dishes:
                    print(f"{num_order}. {dishes}")
                    num_order += 1
                print(f"Total price: {total_cost}")
                print()
                order_confirm = input("Enter y/Y to confirm: ")
                if order_confirm == "y" or order_confirm == "Y":
                    if money >= total_cost:
                        dish_choose_bool = True
                        Customers.money_payment(total_cost, username, password)
                        add_order_txt(username, selected_rest, ordered_dishes, total_cost)
                        print("Order processing...", end = "", flush = True)
                        time.sleep(3)
                        print("\r" + " " * 19 + "\r", end="", flush = True)
                        print("Your order is sent. Please wait patiently.")
                        input("Press ENTER to continue...")
                        return selected_rest, ordered_dishes
                    else:
                        print("Order processing...", end = "", flush = True)
                        time.sleep(3)
                        os.system("cls")
                        print("You don't have enough money.")
                        input("Press ENTER to continue...")
                else:
                    pass
            
            if dish_choose == "":
                dish_choose_bool = True
            
def next_order_id():
    if not os.path.exists("food_order.txt"):
        return 1
    
    orders_file = open("food_order.txt", "r")
    orders_lines = orders_file.readlines()

    if not orders_lines:
        orders_file.close()
        return 1
    max_id = 0

    for line in orders_lines:
        order_elements = line.strip().split(";")
        if order_elements:
            try:
                current_id = int(order_elements[0])
                if current_id > max_id:
                    max_id = current_id
            except ValueError:
                pass
    orders_file.close()
    return max_id + 1

def add_order_txt(username, restaurant, dishes, total_cost):
    order_id = next_order_id()
    ordered_dishes = ",".join(dishes)
    orders_file = open("food_order.txt", "a")
    orders_file.write(f"{order_id};{username};{restaurant};{ordered_dishes};{total_cost}\n")
    orders_file.close()

def get_users_order(username):
    if not os.path.exists("food_order.txt"):
        return []
    
    orders = []
    orders_file = open("food_order.txt", "r")
    for order_line in orders_file:
        order_elements = order_line.strip().split(";")

        if len(order_elements) == 5:
            order_id, customer, restaurant, dishes, total_cost = order_elements
            if customer == username:
                orders.append({
                    "id" : int(order_id),
                    "restaurant" : restaurant,
                    "dishes" : dishes.split(","),
                    "total_cost" : int(total_cost)
                })
    orders_file.close()
    return orders

def get_restaurants_order(restaurant):
    if not os.path.exists("food_order.txt"):
        return []
    
    orders = []
    orders_file = open("food_order.txt", "r")
    for order_line in orders_file:
        order_elements = order_line.strip().split(";")

        if len(order_elements) == 5:
            order_id, customer, rest, dishes, total_cost = order_elements
            if rest == restaurant:
                orders.append({
                    "id" : int(order_id),
                    "username" : customer,
                    "dishes" : dishes.split(","),
                    "total_cost" : int(total_cost)
                })
    orders_file.close()
    return orders

def finished_order(order_id):
    if not os.path.exists("food_order.txt"):
        return False
    order_lines = []
    delete_line = False

    orders_file = open("food_order.txt", "r")
    for line in orders_file:
        order_elements = line.strip().split(";")
        if len(order_elements) == 5 and int(order_elements[0]) == order_id:
            delete_line = True
            continue
        order_lines.append(line)
    orders_file.close()
    
    if delete_line:
        orders_file = open("food_order.txt", "w")
        orders_file.writelines(order_lines)
        orders_file.close()
    return delete_line

def display_user_orders(username):
    os.system("cls")
    orders = get_users_order(username)

    print("============= My Orders =============")
    if not orders:
        print()
        print("You don't have any pending order.")
        input("Press ENTER to continue...")
        return
    
    for num, order in enumerate(orders, 1):
        print(f"{num}. {order['restaurant']}\tTotal cost: ${order['total_cost']}")
        print(f"  Dish: {', '.join(order['dishes'])}")
        print()
    input("Press ENTER to continue...")
    
def manage_restaurant_orders():
    rest_name_found = False
    words = ""

    while not rest_name_found:
        os.system("cls")
        print("============= Order Management =============")
        print("(leave blank to go back)")
        rest_name = input(words + "Enter name of restaurant: ")
        if rest_name == "":
            return
        if rest_name not in restaurant_list:
            words = "Restaurant not found. Please enter again.\n"

        else:
            rest_name_found = True
            words2 = ""
            while True:
                os.system("cls")
                rest_orders = get_restaurants_order(rest_name)
                print(f"============= {rest_name} Orders =============")
                if not rest_orders:
                    print()
                    print(f"{rest_name} doesn't have any pending order.")
                    input("Press ENTER to continue...")
                    break
                
                for num, order in enumerate(rest_orders, 1):
                    print(f" Order ID: {num} | Customer: {order['username']} | Value: ${order['total_cost']}")
                    print(f"  Dish: {', '.join(order['dishes'])}\n")

                try:
                    print("(Enter 0 to go back)" + words2)
                    complete_order = int(input("Enter the order ID to complete the order: "))
                    if complete_order == 0:
                        break
                    if 1 <= complete_order <= len(rest_orders):
                        target_order_id = rest_orders[complete_order - 1]['id']
                        finished_order(target_order_id)
                        print("Order processing...", end = "", flush = True)
                        time.sleep(3)
                        print("\r" + " " * 19 + "\r", end="", flush = True)
                        print("Order completed.")
                        print("Press ENTER to continue...")

                    else:
                        words2 = "\nOrder ID not found. Please try again."

                except ValueError:
                    words2 = "\nPlease enter the order ID (integer)."

def display_rest_details(restaurant):
    rest_file = open("restaurant_test.txt", "r")
    for rest_lines in rest_file:
        rest_elements = rest_lines.strip().split(";")
        if rest_elements[1] == restaurant:
            print(f"========== {restaurant} ==========")
            print(f"Address: {rest_elements[2]}")
            print(f"Open Hours: {rest_elements[7]}")
            print()
            input("Press ENTER to continue...")
            break


# ================================================================================ #

login_pass = False
system_available = True

rest1, rest2, rest3, rest4 = 0, 1, 2, 3

restaurant_objects = Restaurant.load_restaurants("restaurant_test.txt")


restaurant_list = [
    r.get_name()
    for r in restaurant_objects
]

print(" ___         __                  __            ")
print(" /_     _/  /  )_  /,   _  _    (     __/_  _  ")
print("/  ()()(/  /__/(-'(/ \/(-'/ (/ __)(/_) /(-'//) ")
print("                            /     /            ")
input("𝙴𝙽𝚃𝙴𝚁...")
os.system("cls")

while not login_pass:
    os.system("cls")
    print("1. sign in      2. sign up      3. add restaurant      4.restaurant orders      5. exit")
    choose = input("Enter (1/2/3/4/5): ")

    if choose == "1":
        if login_function("account.txt"):
            login_pass = True
    elif choose == "2":
        if create_account():
            login_pass = True
    elif choose == "3":
        os.system("cls")
        print("Add New Restaurant")

        try:
            restaurant_id = len(restaurant_objects) + 1
  
            name = input("Restaurant name: ")
            if name == "":
                continue

            address = input("Address: ")
            store_image = input("Store image: ")
            dining_image = input("Dining image: ")
            kitchen_image = input("Kitchen image: ")
            license_image = input("License image: ")
            business_hours = input("Business hours: ")

            new_restaurant = Restaurant(
                restaurant_id,
                name,
                address,
                store_image,
                dining_image,
                kitchen_image,
                license_image,
                business_hours
            )

            restaurant_objects.append(new_restaurant)

            restaurant_list.append(
                new_restaurant.get_name()
            )
            Restaurant.save_restaurants(
                "restaurant_test.txt",
                restaurant_objects
            )

            print("Restaurant added successfully")

            if not os.path.exists("restaurant_data"):
                 os.makedirs("restaurant_data")

            menu_file_name = f"restaurant_data/{name}_menu.txt"


            print("\nNow create menu for this restaurant.")

            dish_id = 1 

            while True:
                print("\nAdd a dish (leave name blank to finish)")

                dish_type = input("Dish type (e.g. Main, Drink): ")
                dish_name = input("Dish name: ")

                if dish_name == "":
                    break

                price = input("Price: ")
 
                sales = 0

                with open(menu_file_name, "a") as f:
                    f.write(
                        f"{dish_type};{dish_id};{dish_name};{price};{sales}\n"
                    )
                    
                dish_id += 1

            print("Menu created successfully.")

        except Exception as e:
            print("Error:", e)
  
        input("Press ENTER to continue...")

    elif choose == "4":
        manage_restaurant_orders()

    elif choose == "5":
        os.system("cls")
        print(" ___         __                  __            ")
        print(" /_     _/  /  )_  /,   _  _    (     __/_  _  ")
        print("/  ()()(/  /__/(-'(/ \/(-'/ (/ __)(/_) /(-'//) ")
        print("                            /     /            ")
        print("𝚂𝚈𝚂𝚃𝙴𝙼 𝙴𝙽𝙳𝙴𝙳")
        break
    else:
        os.system("cls")
        print("Wrong input.")
    
while login_pass and system_available:

    os.system("cls")

    left_list = False
    right_list = False
    rest_up_limit = 4

    print(f"Food Delivery System\t\t\tmoney: {money} | {current_username}")
    print("--------------------------------------------------" + ("-" * (len(current_username + str(money)))))

    if rest1 != (len(restaurant_list) - 1) and rest2 != (len(restaurant_list) - 1) and rest3 != (len(restaurant_list) - 1):
        print("1. " + restaurant_list[rest1])
        print("2. " + restaurant_list[rest2])
        print("3. " + restaurant_list[rest3])
        print("4. " + restaurant_list[rest4])

        if rest1 == 0 and len(restaurant_list) <= 4:
            print("|\t\t|")
            left_list = True
            right_list = True
        elif rest1 == 0:
            print("|\t\t>")
            left_list = True
        elif rest4 == (len(restaurant_list) - 1):
            print("<\t\t|")
            right_list = True
        else:
            print("<\t\t>")
        
    else:
        if (len(restaurant_list) % 4) == 1:
            print("1. " + restaurant_list[rest1])
            print("2. ----")
            print("3. ----")
            print("4. ----")
            rest_up_limit = 1

        elif (len(restaurant_list) % 4) == 2:
            print("1. " + restaurant_list[rest1])
            print("2. " + restaurant_list[rest2])
            print("3. ----")
            print("4. ----")
            rest_up_limit = 2

        elif (len(restaurant_list) % 4) == 3:
            print("1. " + restaurant_list[rest1])
            print("2. " + restaurant_list[rest2])
            print("3. " + restaurant_list[rest3])
            print("4. ----")
            rest_up_limit = 3

        if rest1 == 0 and len(restaurant_list) <= 3:
            print("|\t\t|")
            left_list = True
            right_list = True
        else:
            print("<\t\t|")
            right_list = True


    print("5. add value\t6. my orders\t7. exit\n")
    rest_choose = input("Enter (1/2/3/4/5/6/7/</>):\n")


    if rest_choose == "1":
            os.system("cls")
            selected_rest = restaurant_list[rest1]
            rest_func_bool = False

            while not rest_func_bool:
                print(selected_rest)
                print("1.menu    2.detail    3.exit")
                rest_func_choose = input("Enter (1/2/3): ")

                if rest_func_choose == "1":
                    food_ordering(selected_rest, current_username, current_password, money)
                    money = refresh_money(current_username, current_password)
                    os.system("cls")

                elif rest_func_choose == "2":
                    os.system("cls")
                    display_rest_details(restaurant_list[rest1])
                    os.system("cls")
                    print()

                elif rest_func_choose == "3":
                    rest_func_bool = True
                else:
                    os.system("cls")
                    print("Wrong input. Please enter again.")

    elif rest_choose == "2":
        if rest_up_limit < 2:
            pass
        else:
            os.system("cls")
            selected_rest = restaurant_list[rest2]
            rest_func_bool = False

            while not rest_func_bool:
                print(restaurant_list[rest2])
                print("1.menu    2.detail    3.exit")
                rest_func_choose = input("Enter (1/2/3): ")

                if rest_func_choose == "1":
                    food_ordering(selected_rest, current_username, current_password, money)
                    money = refresh_money(current_username, current_password)
                    os.system("cls")
                
                elif rest_func_choose == "2":
                    os.system("cls")
                    display_rest_details(restaurant_list[rest2])
                    os.system("cls")
                    print()

                elif rest_func_choose == "3":
                    rest_func_bool = True
                else:
                    os.system("cls")
                    print("Wrong input. Please enter again.")


    elif rest_choose == "3":
        if rest_up_limit < 3:
            pass
        else:
            selected_rest = restaurant_list[rest3]
            os.system("cls")
            rest_func_bool = False

            while not rest_func_bool:
                print(restaurant_list[rest3])
                print("1.menu    2.detail    3.exit")
                rest_func_choose = input("Enter (1/2/3): ")

                if rest_func_choose == "1":
                    food_ordering(selected_rest, current_username, current_password, money)
                    money = refresh_money(current_username, current_password)
                    os.system("cls")

                elif rest_func_choose == "2":
                    os.system("cls")
                    display_rest_details(restaurant_list[rest3])
                    os.system("cls")
                    print()

                elif rest_func_choose == "3":
                    rest_func_bool = True
                else:
                    os.system("cls")
                    print("Wrong input. Please enter again.")


    elif rest_choose == "4":
        if rest_up_limit < 4:
            pass
        else:
            os.system("cls")
            selected_rest = restaurant_list[rest4]
            rest_func_bool = False

            while not rest_func_bool:
                print(restaurant_list[rest4])
                print("1.menu    2.detail    3.exit")
                rest_func_choose = input("Enter (1/2/3): ")
                if rest_func_choose == "1":
                    food_ordering(selected_rest, current_username, current_password, money)
                    money = refresh_money(current_username, current_password)
                    os.system("cls")

                elif rest_func_choose == "2":
                    os.system("cls")
                    display_rest_details(restaurant_list[rest3])
                    os.system("cls")
                    print()

                elif rest_func_choose == "3":
                    rest_func_bool = True
                else:
                    os.system("cls")
                    print("Wrong input. Please enter again.")


    elif rest_choose == "5":
        os.system("cls")
        Customers.add_money(current_username, current_password)
        money = refresh_money(current_username, current_password)
        pass

    elif rest_choose == "<":
        if not left_list:
            rest1 -= 4
            rest2 -= 4
            rest3 -= 4
            rest4 -= 4

    elif rest_choose == ">":
        if not right_list:
            rest1 += 4
            rest2 += 4
            rest3 += 4
            rest4 += 4

    elif rest_choose == "6":
        display_user_orders(current_username)

    elif rest_choose == "7":
        os.system("cls")
        print(" ___         __                  __            ")
        print(" /_     _/  /  )_  /,   _  _    (     __/_  _  ")
        print("/  ()()(/  /__/(-'(/ \/(-'/ (/ __)(/_) /(-'//) ")
        print("                            /     /            ")
        print("𝚂𝚈𝚂𝚃𝙴𝙼 𝙴𝙽𝙳𝙴𝙳")
        system_available = False
    else:
        pass
