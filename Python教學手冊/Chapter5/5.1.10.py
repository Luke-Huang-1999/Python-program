# 完美數定義：一個正整數的所有「正因數（不包含自己）」加總後，恰好等於它本身。
def factor(n):
    # 尋找小於n的因數
    list1 = []
    for i in range(1, n):
        if n % i == 0:
            list1.append(i)
    return list1


def checkPerfect(max):
    perfectList = []
    for i in range(1, max + 1):
        list1 = factor(i)
        total = 0
        for j in range(0, len(list1)):
            total += list1[j]
        if total == i:
            perfectList.append(i)

    return perfectList

#尋找四位數以內的所有完美數
print(checkPerfect(9999))
