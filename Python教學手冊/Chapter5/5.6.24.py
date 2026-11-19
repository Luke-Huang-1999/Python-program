def sign(x):
    if(x>= 0):
        return 1
    else:
        return -1

sign_Lam = lambda x: 1 if (x >= 0) else -1


print(sign(10))
print(sign_Lam(10))
print(sign_Lam(-1))

lst = [9,-3,8,2,1,-1,-4]
lst2 = [sign_Lam(lst[i]) for i in range(0, len(lst))]
print(lst2)


sign2 = lambda x: 1 if (x > 0) else (0 if x == 0 else -1)

print(sign2(-10))
print(sign2(0))
print(sign2(10))