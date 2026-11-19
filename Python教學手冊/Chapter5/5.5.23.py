def fib_for(n):
    fib_list = []
    for i in range(0, 2):
        fib_list.append(1)

    for j in range(2, n):
        fib_list.append(fib_list[j - 1] + fib_list[j - 2])

    print(fib_list)
    return fib_list[n - 1]


def fib_recursive(n):
    if n > 2:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    elif n == 1 or n == 2:
        return 1


print(fib_for(40))
print(fib_recursive(40))

# 1 2 3 4 5 6  7  8
# 0 1 2 3 4 5  6  7
# 1 1 2 3 5 8 13 21
# 遞迴較符合數學直覺操作，
# 但當n很大時，
# 會不斷呼叫函數，
# 造成運行非常慢

# for迴圈很快很好debug，實務上建議用for迴圈為主，遞迴為輔
#