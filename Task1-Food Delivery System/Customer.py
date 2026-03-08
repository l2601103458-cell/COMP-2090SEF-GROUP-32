class Customers:
    account_list = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.money = 0
        Customers.account_list.append(self.username + ";" + self.password)
    
    def add_money(self):
        money = int(input("How many you want to add: "))
        self.money += money
        print(self.money)
