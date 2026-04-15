import os
class Customers:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.money = 0

    @staticmethod
    def create_acc(username, password):
        money = 0
        acc_file = open("account.txt", "a")
        acc_file.write(f"{username};{password};{money}\n")
        acc_file.close()

    @staticmethod
    def add_money(username, password):
        acc_list = []

        acc_file = open("account.txt", "r")
        acc_lines = acc_file.readlines()
        for get_acc_data in acc_lines:
            acc_data = get_acc_data.strip().split(";")
            if username == acc_data[0] and password == acc_data[1]:
                if acc_data[2].isdigit():
                    now_money = int(acc_data[2])
                    acc_list.append(" ")
                else:
                    os.system("cls")
                    print("Error occured. Please try again later.")
                    print("Press ENTER to go back")
                    input()
                    return
            else:
                acc_list.append(get_acc_data)
        acc_file.close()

        while True:
            while True:
                print("(Leave blank to go back)")
                print("Amount you want to add:")

                try:
                    addition = input("Enter (integer): ")
                    if addition.isdigit():
                        addition = int(addition)
                        if addition > 0:

                            acc_file = open("account.txt", "w")
                            for new_acc_lines in acc_list:
                                if new_acc_lines == " ":
                                    acc_file.write(f"{username};{password};{now_money + addition}\n")
                                else:
                                    acc_file.write(new_acc_lines)
                            print("Processing complete.")
                            print("Press ENTER to go back")
                            input()
                            acc_file.close()
                            return
                        
                        else:
                            os.system("cls")
                            print("The input is not positive. Please try again.")

                    elif addition == "":
                        return
                    else:
                        os.system("cls")
                        print("The input is not an integer. Please try again.")

                except ValueError:
                    os.system("cls")
                    print("The input is not an integer. Please try again.")

    @staticmethod
    def money_payment(total_cost, username, password):
        acc_list = []

        acc_file = open("account.txt", "r")
        acc_lines = acc_file.readlines()
        for get_acc_data in acc_lines:
            acc_data = get_acc_data.strip().split(";")
            if username == acc_data[0] and password == acc_data[1]:
                if acc_data[2].isdigit():
                    now_money = int(acc_data[2])
                    acc_list.append(" ")
            else:
                acc_list.append(get_acc_data)
        acc_file.close()

        acc_file = open("account.txt", "w")
        for new_acc_lines in acc_list:
            if new_acc_lines == " ":
                acc_file.write(f"{username};{password};{now_money - total_cost}\n")
            else:
                acc_file.write(new_acc_lines)
        acc_file.close()
        return