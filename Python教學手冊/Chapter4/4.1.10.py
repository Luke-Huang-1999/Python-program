hour = int(input("請輸入停車小時數："))
money = 0
if(hour > 12):
    money = 12 * 40 + (hour - 12)* 30
else:
    money = hour * 40

print(f"停車時數為{hour}，停車費共{money}元")
    

