def factor(n):
    lst = []
    for i in range(1, n+1):
        if(n % i == 0):
            lst.append(i)
    return lst


def primes(n):
    lst = [2]
    for i in range(3, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            lst.append(i)
    return lst