d1 = {0: "red", 1: "green", 2: "blue"}
print(f"a = {d1.get(1)}")


d1.update({2: "yellow"})
print(f"b = {d1.items()}")

d1.pop(0)
print(f"c = {d1.items()}")

print(f"d = {4 in d1}")
