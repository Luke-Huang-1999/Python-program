def prime_factors(n):
    lst = []
    i = 2
    while n != 1:
        if is_primes(i) and n % i == 0:
            n = n / i
            lst.append(i)
        else:
            i += 1
    return lst


def is_primes(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True