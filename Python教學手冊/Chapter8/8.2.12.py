def to_byteArray(lst):
    try:
        for i in lst:
            if(not isinstance(i, int)):
                raise TypeError("不是int")
            if(i > 2**8):
                raise ValueError("數字過大")

    except ValueError as e:
        print(f"數字超過範圍：{e}")
    except TypeError as e:
        print(f"類型不對：{e}")
    else:
        return bytes(lst)

lst = [1, "a", 3]

print(to_byteArray(lst))
