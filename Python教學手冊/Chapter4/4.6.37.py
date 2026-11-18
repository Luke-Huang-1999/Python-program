num1 = [1,2,3]
num2 = [4,5]

result = [[num1[i], num2[j]] for i in range(0, len(num1)) for j in range(0, len(num2))]
print(result)