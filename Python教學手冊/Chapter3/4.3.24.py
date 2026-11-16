str1 = "machine_learning"
index = 0
while index < len(str1):
    if str1[index].isalpha():
        index += 1
    else:
        break

print(f"不是英文字元的索引值為{index}")
