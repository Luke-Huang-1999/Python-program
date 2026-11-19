def fib(n):
    lst = []
    lst.append(1)
    lst.append(1)

    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    print(lst)

    return lst[n - 1]

def fib_gen(n):
    lst = [1, 1]

    yield lst[0]
    yield lst[1]

    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
        yield lst[i]
fib_obj = fib_gen(10)
print(next(fib_obj))
print(next(fib_obj))
print(next(fib_obj))

#for num in fib_gen(10):
#    print(num)

#print(fib_gen(10))