d1 = {"large": 34, "medium": 28, "small": 20}

lst = list(d1.keys())
print(f"a = {lst}")

tpl = tuple(d1.values())
print(f"b = {tpl}")


# [('large', 34), ('medium', 28), ('small', 20)]
c = list(d1.items())
print(f"c = {c}")

d1.setdefault("large", 36)
print(f"d = {d1}")
# 因為large已經存在，所以維持對應的值34
# 若不存在則建立一個"large":36的鍵值對

d1.setdefault("xlarge", 40)
print(f"e = {d1}")

# 排序
d1 = dict(sorted(d1.items(), key = lambda x:x[1], reverse=True))
print(d1)