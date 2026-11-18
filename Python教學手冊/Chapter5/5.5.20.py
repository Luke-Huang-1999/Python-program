def total(n):#遞迴函數Recursion
    if(n != 1):
        return n + total(n-1)
    else:#終止條件 Base case
        return 1

print(total(10))