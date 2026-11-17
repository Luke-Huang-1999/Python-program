lower_limit = 0
upper_limit = 255


num1 = input("請輸入一串數字，用逗號分隔：")
num1 = num1.split(",")
cnt = len(num1)
for i in range(0, len(num1)):
    if(not lower_limit <= int(num1[i]) <= upper_limit):
        print(f"輸入的數不在[{lower_limit}, {upper_limit}]之內")
        break
else:
    print(f"所有的數都在[{lower_limit}, {upper_limit}]之內")


#9,12,-1,32,-8