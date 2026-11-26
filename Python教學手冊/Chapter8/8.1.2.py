num = 100
lst = [i for i in range(1, 101) if num % i == 0]
print(lst)

with open("ex8_2.txt", "w", encoding="utf-8") as file:
    for i in range(0, len(lst)):
        file.write(str(lst[i]))
        if i != len(lst) - 1:
            file.write(", ")

total = 0
with open("ex8_2.txt", "r", encoding="utf-8") as file:
    data = file.read()
    lst_2 = [int(nums) for nums in data.split(", ")]

for i in lst_2:
    total += i
print(total)

with open("ex8_2.bin", "wb") as file:
    file.write(bytes(lst))

total_b = 0
with open("ex8_2.bin", "rb") as file:
    data = file.read()
    for i in data:
        total_b += i
print(total_b)
