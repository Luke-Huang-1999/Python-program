class EasyCard:
    def __init__(self, owner, amount = 0):
        self.name = owner
        self.balance = amount
        print(f"{self.name}新卡儲值{amount}")
    def add_value(self, amount):
        self.balance += amount
        print(f"{self.name}儲值{amount}，餘額：{self.balance}")
    def spend(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            print(f"{self.name}消費{amount}，餘額：{self.balance}")
        else:
            print("餘額不足")

ac1 = EasyCard("Mary", 50)
ac1.add_value(300)
ac1.spend(200)
ac1.spend(400)
ac2= EasyCard("Tom", 100)
ac2.spend(20)