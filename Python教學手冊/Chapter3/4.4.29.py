num = [47, 89, 12, -4, 12, 2, 97]
index = 0
i = num[index]
#print(len(num))  # 7
while index < len(num):
    print(f"{num[index]}")
    if num[index] < 0:
        break
    index += 1
