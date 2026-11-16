temp = int(input("請輸入目前溫度："))
if(temp > 28):
    print(f"現在氣溫為{temp}度，開冷氣")
elif(temp < 15):
    print(f"現在氣溫為{temp}度，開暖氣")
else:
    print(f"現在溫度為{temp}度，不開冷暖氣")