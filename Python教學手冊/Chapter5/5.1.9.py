def n_digits(num):
    n = 0  # 記錄幾位數
    while True:
        num = num // 10
        n += 1
        if(num < 1):
            break
    return n

print(n_digits(100))