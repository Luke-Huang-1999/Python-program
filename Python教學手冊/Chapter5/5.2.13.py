def add100(lst):
    lst[0] += 100
    return lst

lst = [10,20,30]

print(add100(lst))

#因為函數參數為串列時，
#程式會降級為傳送第一個元素的記憶體位址，
#更改內部元素值會直接更改內部資料，
#這種傳遞參數的方法又稱為"Python 的共享物件傳遞（Call by Sharing）"
