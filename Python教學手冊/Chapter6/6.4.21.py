def make_dict(keys=None, values=None):
    d1 = {}
    if values == None:
        values = [0] * len(keys)

    for i in range(0, len(keys)):
        d1.setdefault(keys[i], values[i])

    return d1

keys = [0, 1, 2]
d2 = make_dict(keys)
print(d2)


keys = [0, 1, 2]
values = [32, 43, 55]
d1 = make_dict(keys, values)
print(d1)

