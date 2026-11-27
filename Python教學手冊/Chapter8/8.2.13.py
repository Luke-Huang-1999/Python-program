try:
    age = input("請使用者輸入年齡：")
    if(not age.lstrip("-").isdigit()):
        raise ValueError("請輸入數字")
    if(int(age) < 18):
        raise ValueError("年齡不能小於18歲")
    else:
        print(f"年齡為{age}歲")
except ValueError as e:
    print(f"錯誤訊息：{e}")