def primes(n):
    yield 2

    for i in range(3, n + 1):
        check = True
        for j in range(2, i):
            if(i % j == 0):
                check = False
        if(check):
            yield i

for i in primes(11):
    print(i)