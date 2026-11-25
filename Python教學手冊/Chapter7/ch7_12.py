class BankAccount:
    def __init__(self, Balance):
        self.__balance = Balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print(f"存入{amount}元，餘額{self.__balance}元")
    def withdraw(self, amount):
        if(0<amount<=self.__balance):
            self.__balance -= amount
            print(f"取出{amount}元，餘額{self.__balance}元")
        else:
            print("餘額不足")

acc = BankAccount(1000)
print(f"帳戶餘額{acc.get_balance()}元")
acc.deposit(500)
acc.withdraw(200)

    