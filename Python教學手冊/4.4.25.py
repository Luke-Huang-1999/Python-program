i = 1
a = []

while i <= 10:
    if i % 3 != 0:
        a.append(i)
    i += 1

print(f"不能被3整除的數有{a}")
