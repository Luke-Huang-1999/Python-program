month = int(input("請輸入一個月份："))
if month >= 3 and month <= 5:
    print("春季")
elif month >= 6 and month <= 8:
    print("夏季")
elif month >= 9 and month <= 11:
    print("秋季")
elif month == 12 or 0 < month <= 2:
    print("冬季")
