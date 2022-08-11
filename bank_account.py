from user import User


# child class - pass user class as args
class Bank(User):
    # no param constructor
    '''def __init__(self):
        name = None
        age = None
        gender = None
        address = None
        balance =0
    '''

    def __init__(self, name, age, gender, address):
        super().__init__(name, age, gender, address)
        self.balance = 0

    def set_balance(self, amount):
        self.balance = amount

    def get_balance(self):
        return self.balance

    def get_details(self):
        super().get_user_details()
        print("Account balance: ", self.balance)
        print()

    def make_a_deposit(self, amount):
        print("Deposit Transaction")
        print("--------------------")
        self.balance += amount
        print("account balance has been updated. ", self.balance)

    def make_a_withdraw(self, amount):
        print("Withdraw Transaction")
        print("--------------------")
        # check if balance is greater than amount
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
            print("Initial balance: ", self.balance + amount)
            print("New balance: ", self.balance)
        else:
            print("Insufficient balance  ")
        print()

    def make_atm_withdraw(self, amount):
        print("Withdraw Transaction")
        print("--------------------")
        if self.balance >= amount:
            self.balance -= amount + 2.5
            print("You Withdrew:", amount)
            print("transaction fee: ", 2.5)
            print("Initial balance: ", self.balance + (amount + 2.5))
            print("New balance: ", self.balance)
        else:
            print("Insufficient balance  ")
        print()
