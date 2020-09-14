class BankAccount():
    def __init__(self, kind, pin):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        self.balance
    
    def withdraw(self, amount, pin_from_user):
        if (self.pin == pin_from_user):
            if (self.balance < amount):
                print("My dude, you don't got that money")
                # self.overdraft_fees
            elif (self.balance == amount):
                self.balance -= amount
                print("You just withdrew all your money and now you are done")
            if (self.balance > amount):
                self.balance -= amount
            return amount
        print("Invalid pin number")
    
    def change_pin(self, pin):
        self.pin = pin
        print("The new pin number is {self.pin}")

rome_checking = BankAccount("checking", 1234)
# print("My new account is a {} account".format(rome_checking.kind))

rome_checking.deposit(3000)
# print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.withdraw(1500, 1243)
# print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.withdraw(3000, 1234)
# print("My overdraft fee is currently {}.".format(rome_checking.overdraft_fees))