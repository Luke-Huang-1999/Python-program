# def invert_dict(d1):
#     # 資料轉換Dict->List
#     d1 = list(d1.items())
#     for i in range(0, len(d1)):
#         d1[i] = list(d1[i])
#     # 交換
#     for i in range(0, len(d1)):
#         tmp = d1[i][0]
#         d1[i][0] = d1[i][1]
#         d1[i][1] = tmp

#     # 變回dict
#     d2 = {}
#     for i in range(0, len(d1)):
#         d2.setdefault(d1[i][0], d1[i][1])
#     print(d2)

# d = {"a": 1, "b": 2, "c": 3}
# invert_dict(d)


def invert_dict(d1):
    d2 = {}
    for key, value in d1.items():
        d2[value] = key
    return d2

d = {"a": 1, "b": 2, "c": 3}
print(invert_dict(d))
