def primes(x):
    result = []
    result.append(2)

    for i in range(3, x + 1):
        status = True  # default  prime

        for j in range(2, i - 1):
            if i % j == 0:  # not prime
                status = False
                break

        if status ==True:
            result.append(i)
    return result


print(primes(10))