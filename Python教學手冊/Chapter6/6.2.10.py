def find_value(tpl, target):
    for i in tpl:
        if i == target:
            return tpl.index(i)
    else:
        return -1


tpl = (10, 20, 30, 40)
target = 30
print(find_value(tpl, target))
