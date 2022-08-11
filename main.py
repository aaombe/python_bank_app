from bank_account import Bank


def create_new_user():
    # get user input
    name = input("Enter name: ")
    age = input("Enter age : ")
    gender = input("Enter gender: ")
    address = input("Enter your address: ")
    deposit = get_amount()  # call get_amount() to get a valid input
    print()  # print new line

    # create new user object
    user = Bank(name, age, gender, address)
    user.set_balance(deposit)

    return user


# prompt user to enter amount not less than zero
def get_amount():
    while True:
        deposit = float(input("Enter amount for the transaction: "))
        if deposit < 0:
            print("Invalid amount ")
        else:
            return deposit


# prompt user to select a valid transaction
def type_of_transaction():
    print("Select from the following transaction")
    print("Enter: 1. Deposit \t 2. Withdraw from bank \t 3. With from atm")
    while True:
        ttype = input("Enter your selection: ")
        if ttype not in "1 2 3":
            print("Invalid")
        else:
            return int(ttype)


def make_transaction(user):
    traction = type_of_transaction()
    if traction == 1:
        user.make_a_deposit(get_amount())
    elif traction == 2:
        user.make_a_withdraw(get_amount())
    else:
        user.make_atm_withdraw(get_amount())


if __name__ == '__main__':
    user_1 = create_new_user()
    user_1.get_details()
    make_transaction(user_1)
    user_1.get_details()
