num = int(input("請輸入一個整數："))
num2 = num
result = 1

for _ in range(0, num):
    result = result * num
    num -= 1

print(f"{num2}階乘結果為{result}")
