while(True):
    password = input("請輸入密碼：")

    if(not password.isalnum()):
        print("密碼只能包含英文字母或數字")

    if(len(password) < 6):
        print("密碼長度至少6個字元")

    if(password.isalnum() and len(password) >= 6):
        print("密碼設定成功")
        break