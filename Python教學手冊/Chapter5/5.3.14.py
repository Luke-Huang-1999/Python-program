def add_n(lst, n=0):
    for i in range(0, len(lst)):
        lst[i] += n
    return lst


lst = [10, 20, 30]
print(add_n(lst, 3))
