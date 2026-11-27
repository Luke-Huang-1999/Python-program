while True:
    try:
        input_1 = input("請輸入分子(輸入 exit 結束程式)：")

        if input_1 == "exit":
            break

        if not input_1.lstrip("-").isdigit():
            raise ValueError("不是數字")

        input_2 = input("請輸入分母：")
        if not input_2.lstrip("-").isdigit():
            raise ValueError("不是數字")
        if int(input_2.lstrip("-")) == 0:
            raise ZeroDivisionError("分母為0")


    except ValueError as e:
        print(f"輸入的不是數字：{e}")
    except ZeroDivisionError as e:
        print(f"分母為0：{e}")
    else:
        # if input_1 in "-":
        #     input_1 = int(input_1.lstrip("-")) * -1
        # else:
        #     input_1 = int(input_1)
        # if input_2 in "-":
        #     input_2 = int(input_2.lstrip("-")) * -1
        # else:
        #     input_2 = int(input_2)
        input_1 = int(input_1)
        input_2 = int(input_2)
        print(f"{input_1} / {input_2} = {input_1 / input_2}")
        print("程式計算完成")
