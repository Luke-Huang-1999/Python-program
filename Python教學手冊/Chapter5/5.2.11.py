def square(lst):
    lst2 = []
    for i in range(0, len(lst)):
        lst2.append(lst[i] ** 2)
    return lst2

lst = [1,2,3,4,5,6]
print(square(lst))