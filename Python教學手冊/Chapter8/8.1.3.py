lst = [[23, 45, 23, 65], [44, 56, 88, 21], [50, 67, 89, 12]]
print(lst)
with open("ex8_3.txt", "w", encoding="utf-8") as file:
    for row in lst:
        for nums in row:
            file.write(str(nums) + " ")
        file.write("\n")

with open("ex8_3.txt", "r") as file:
    data = file.read()

data = [int(nums) for nums in data.split()]
print(f"最大值 = {max(data)}")
print(f"最小值 = {min(data)}")
