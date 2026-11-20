lst = [9, 8, 7, 1, 2, 3, 7, 3, 2]

a = []
for i in range(0, 3):
    a.append(lst[i])
print(f"a = {a}")


b = []
for i in range(len(lst) - 3, len(lst)):
    b.append(lst[i])
print(f"b = {b}")

c = []
for i in range(4, 8):
    c.append(lst[i])
print(f"c = {c}")

d = []
for i in range(1, len(lst)):
    if lst[i] % 2 == 0:  # 偶數
        d.append(lst[i])
print(f"d = {d}")

# e
Max = max(lst)
Min = min(lst)
length = len(lst)
print(f"lst最大值 = {Max}")
print(f"lst最小值 = {Min}")
print(f"lst長度 = {length}")

# f
# lst[start:end:step]
print(lst[-1:-5:-1])

lst.reverse()
print(lst)