import ex8_15_m1 as M1


def is_prime(p):
    if len(M1.factors(p)) == 2:
        return True
    else:
        return False


print(is_prime(10))
