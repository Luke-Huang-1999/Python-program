month = ["Jan", "Feb", "Mar"]
d1 = dict.fromkeys(month)
print(f"a = {d1}")

for i in range(0, 3):
    d1[month[i]] = i + 1
print(f"b = {d1}")

d1.update({"Apr":4})
print(f"c = {d1}")

d1.pop("Feb")
print(f"d = {d1}")
