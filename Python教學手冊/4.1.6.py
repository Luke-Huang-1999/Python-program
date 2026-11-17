a = []
for i in range(0, 3):
    a.append(int(input("請輸入三個整數：")))
print(a)

for i in range(0, 2):
    for j in range(0, 2):
        if a[j] < a[j + 1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp

print(a)
