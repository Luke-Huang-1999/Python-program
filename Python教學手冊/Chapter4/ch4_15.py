import random

target = random.randint(1, 10)
guess = 0

while guess != target:
    guess = int(input("猜一個1~10的數字："))
    if(guess < target):
        print("太小了!請再試一次")
    elif(guess > target):
        print("太大了!請再試一次")

print("恭喜答對!")

