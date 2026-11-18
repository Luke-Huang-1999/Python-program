def bin2dec(bs):
    if(bs == 0):
        return None

    binNumList = list(str(bs))
    binNumList.reverse()
    # print(binNumList)
    decNum = 0
    for i in range(len(binNumList)):
        decNum += int(binNumList[i]) * 2**i
    return decNum


print(bin2dec(1011))
