def primes():
    yield 2
    num = 3
    test_num = 2
    while True:
        check = True
        for i in range(2, num):
            if(num % i == 0):
                check = False
                break
        if(check):
            yield num

        num +=1

primes_obj = primes()
print(next(primes_obj))
print(next(primes_obj))
print(next(primes_obj))
print(next(primes_obj))
print(next(primes_obj))
print(next(primes_obj))
print(next(primes_obj)) 
