class NumberUtils:
    @staticmethod
    def is_prime(n):
        if(n == 2):
            return True
        for i in range(2,n):
            if(n % i == 0):
                return False
        else:
            return True

print(NumberUtils.is_prime(11))
print(NumberUtils.is_prime(15))