import os
from customer import Customers
def login_function(list):
    os.system("cls")
    print("Login")
    login = False
    while not login:
        print("(leave blank to go back)")
        print()
        username = input("Username: ")
        if username == "":
            os.system("cls")
            break
        password = input("Password: ")
        if password == "":
            os.system("cls")
            break
        for account in list:
            un, pw = account.split(";", 1)
            if username == un and password == pw:
                print("Login success.")
                login = True
                return True
        os.system("cls")
        print("Wrong username or password. Please try again.")

def create_account():
    have_upper = False
    have_lower = False
    have_number = False
    create_pass = False

    while not create_pass:
        os.system("cls")
        print("Requirements of creating account:")
        print("1. Length of username should not excceed 12 characters")
        print("2. Length of password should be at least 8 characters")
        print("3. The password should consist of at least 1 uppercase letter, 1 lowercase letter and 1 number")
        print("(leave blank to go back)")
        print()
        new_username = input("Enter your username: ")
        if new_username == "":
            os.system("cls")
            break
        if len(new_username) > 12:
            print("Requirement 1 not fulfilled. Please enter again.")
            continue
        new_password = input("Enter your password: ")
        if new_password == "":
            os.system("cls")
            break
        if len(new_password) < 8:
            print("Requirment 2 not fulfilled. Please enter again.")
            continue
        for letters in new_password:
            if letters.isupper():
                have_upper = True
            if letters.islower():
                have_lower = True
            if letters.isdigit():
                have_number = True
        if have_upper and have_lower and have_number:
            Customers(new_username, new_password)
            create_pass = True
            return True
        else:
            print("Requirement 3 not fulfilled. Please enter again.")
            continue


account1 = Customers("12345678", "ShuaiGe123")
account2 = Customers("87654321", "HiHi1234")
account3 = Customers("12341234", "Abcd1234")

login_pass = False
while not login_pass:
    print("1. sign in\t2. sign up\t3. exit")
    choose = input("Enter (1/2): ")
    if choose == "1":
        if login_function(Customers.account_list):
            login_pass = True
    elif choose == "2":
        if create_account():
            login_pass = True
    elif choose == "3":
        print("System ended")
        break
    else:
        os.system("cls")
        print("Wrong input.")
    

print(Customers.account_list)
