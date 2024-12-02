class Bank:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.balance = balance

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        amount = self.balance + amount
        print(amount)

    def check_acc_num(self, isAuth):
        if isAuth == True:
            print("allowed and acc number is", self.__account_number)
        else:
            print("not allowed")

    def __internal_private_method(self):
        print("private method can be accessed only by class")

    def test(self):
        self.__internal_private_method()


obj_ref = Bank(2122212323, 100)
obj_ref.check_balance()
obj_ref.deposit(200)
print(obj_ref.balance)
# print(obj_ref.__account_number) #AttributeError: 'Bank' object has no attribute '__account_number'. Did you mean: '_Bank__account_number'?
obj_ref.check_acc_num(True)
obj_ref.test()

