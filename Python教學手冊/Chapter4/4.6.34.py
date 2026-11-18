import math

num1 = [int(math.pow(i, 2)) for i in range(1, 11)]

print(num1)

num2 = [i for i in range(1, 51) if i % 3 == 0 and i % 4 == 0]
print(num2)

str1 = "List Comprehension"
str2 = [
    str1[i]
    for i in range(0, len(str1))
    if str1[i] in "aeiou"
]
print(str2)

num3 = [3,-1,4,7,-3,2]
num4 = [1 if num3[i] > 0 else -1 for i in range(0, len(num3))]
print(num4)