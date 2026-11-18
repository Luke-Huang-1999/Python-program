x = "amazing"

def func():
    x = "impressive"
    print(f"Python is {x}")

func()
print(f"Python is {x}")

# x 在函數外使用全域變數，值為 amazing。
# x 在函數內建立區域變數，值為 impressive。
# 兩者是不同的變數，不會互相影響。
