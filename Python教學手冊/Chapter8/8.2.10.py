num = input("請輸入一個數字：")
try:
    if(not num.isdigit()):
        raise ValueError("必須輸入數字")
    if(int(num) < 0):
        raise TypeError("不能輸入負數")

except ValueError as e:
    print(f"輸入錯誤：{e}")
except TypeError as e:
    print(f"數字範圍錯誤：{e}")
    