
time = int(input("請輸入一個整數"))

hour = time / (60 * 60)
mins = (time - int(hour) * (60 * 60)) / 60
sec = time - int(hour) * (60 * 60) - int(mins) * 60
print(f"{time}秒等於{int(hour):02d}小時{int(mins):02d}分{int(sec):02d}秒")
