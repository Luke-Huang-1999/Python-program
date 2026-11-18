def r_pow(base, n):
    if(n != 0):
        return base * r_pow(base, n-1)
    else:
        return 1

print(r_pow(2, 8))