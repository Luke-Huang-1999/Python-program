def to_numbes(word):
    table = [
        [2, "ABC"],
        [3, "DEF"],
        [4, "GHI"],
        [5, "JKL"],
        [6, "MNO"],
        [7, "PQRS"],
        [8, "TUV"],
        [9, "WXYZ"],
    ]
    str1 = str(word)
    numList = []
    for i in range(0, len(str1)):
        for j in range(0, len(table)):
            if str1[i] in table[j][1]:
                numList.append(table[j][0])
                break
    return numList


print(to_numbes("PYTHON"))
