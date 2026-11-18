def factor(x):
    # 找出小於x的質數，並儲存於串列primeList
    primeList = []
    primeList.append(2)

    for i in range(3, x):

        primeCheck = True

        for j in range(2, i):
            if i % j == 0:  # not prime
                primeCheck = False
                break

        if primeCheck:
            primeList.append(i)

    # 模擬短除法
    num = x
    index = 0
    result = []  # 宣告result是陣列，不管未來是一維陣列還是二維陣列...，就是陣列
    while num > 1:
        power = 0
        while num % primeList[index] == 0:
            num = num // primeList[index]  # //整數除法，結果會是int，不會是float浮點數
            power += 1
        if power != 0:
            result.append([primeList[index], power])

        index += 1
    return result


print(factor(72))
