# 1
f1 = lambda x:x if x>0 else -x

print(f1(-10))
print(f1(10))


# 2
f2 = lambda x :True if (x % 2 == 0) else False

print(f2(9))
print(f2(10))


# 3
lst = [1,2,3]
f3 = lambda lst: sum([i**2 for i in lst])

print(f3(lst))

#4
lst2 = [1,2,3,4,5,6,7,8,9,10]
f4 = lambda lst:[i for i in lst if (i % 2 == 0)]
f4_2 = lambda lst:[lst2[i] for i in range(0, len(lst)) if (lst2[i] % 2 == 0)]

print(f4(lst2))
print(f4_2(lst2))



