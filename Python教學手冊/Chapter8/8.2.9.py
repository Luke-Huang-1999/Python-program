while(True):
    try:
        num1 = input("請輸入數字1：")
        if(num1 == 'Q' or num1 == 'q'):
            print("程式結束")
            break
        num2 = input("請輸入數字2：")
        num1 = int(num1)
        num2 = int(num2)

    except ValueError as e:
        print(f"無法判別大小，請重新輸入，詳情：{e}")
    else:
        if(num1 > num2):
            print(f"{num1}大於{num2}")
        elif(num1<num2):
            print(f"{num1}小於{num2}")
        else:
            print(f"{num1}等於{num2}")

        print("判斷完成")


