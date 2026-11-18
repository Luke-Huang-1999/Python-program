def r_sum(n):
    if n != 0:
        total = n * (n - 1)
        return total + r_sum(n - 1)
    else:
        return 0


print(r_sum(5))

# 因為sum是Python的內建函數，
# 不要使用到sum，
# 改用total
