try:
    num = int(input("請輸入一個數字："))
    result = 10/ num
except ZeroDivisionError as e:
    print(f"錯誤詳情：{e}")
except ValueError as e:
    print(f"錯誤詳情：{e}")
else:
    print(f"計算結果為{result}")
finally:
    print("程式執行結束")