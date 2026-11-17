

str1 = input("請輸入一個字串：")

for i in range(0, len(str1)):
    if(str1[i].isdigit() == False):
        print("輸入的數包含不合法的字元")
        break
else:
    print(f"{str1}")

