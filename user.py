class User:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def get_user_details(self):
        print("User Details")
        print("------------")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Address: ", self.address)
