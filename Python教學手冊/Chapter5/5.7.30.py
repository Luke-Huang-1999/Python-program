a = (45, 33, 75)
b = (109, 85, 63)
c = (9, 8, 5)
#z = list(zip(a,b,c))
#print(len(z)) #3
z = [list(i) for i in zip(a, b, c)]
print(z)


lst = [1,2,3,4,5]
for i in lst:
    print(i)