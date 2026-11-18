counter = 0


def increment():
    counter += 1


def get_counter():
    return counter


increment()
increment()
increment()

get_counter()

# 呼叫increment()時，
# 由於counter是全域變數，
# 在increment()內並未被初始化，
#若要更動全域變數的counter，
#需要用global，
#告訴Python函數內使用的counter是外部已經宣告的全域變數，
#不要將他視為increment()內部的區域變數
