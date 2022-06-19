#Parent Class
class User():
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def get_details(self):
        print("User Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Phone Number: ", self.phone)

#Child Class
class Bank(User):
    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited", amount, ".", "Account Aalance:", self.balance)

    def withdraw(self, amount):
        if(amount > self.balance):
            print("<<< Insufficient Funds >>> Balance Available:", self.balance)
            return
        self.balance = self.balance - amount
        print("Withdrawn", amount, "Account Balance:", self.balance)
    
    def get_balance(self):
        self.get_details()
        print("Account Balance:", self.balance)