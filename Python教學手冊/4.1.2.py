num = int(input("請輸入一個整數："))
if(num != 0):
    if(num % 2 == 0):
        print(f"{num}是偶數")
    elif(num % 2 != 0):
        print(f"{num}是奇數")
else:
    print(f"num為0，不為偶數也不為奇數")