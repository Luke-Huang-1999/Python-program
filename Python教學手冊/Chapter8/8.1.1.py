with open("ex8_1.txt", "w", encoding="utf-8") as f:
    f.write("Python")

lst = []
with open("ex8_1.txt", "r", encoding="utf-8") as f:
    for char in f.read():
        lst.append(char)

print(lst)
