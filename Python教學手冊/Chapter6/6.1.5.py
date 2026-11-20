print("lst = [43, 12, 12, 34]")
# a
lst_a = [43, 12, 12, 34]
# 方法1
# lst.extend([2, 12])

# 方法2
lst_a.append(2)
lst_a.append(12)

# 以上2種方法都可以
print(f"a = {lst_a}")

# b
lst_b = [43, 12, 12, 34]
lst_b.append([25, 99])
print(f"b = {lst_b}")

# c
lst_c = [43, 12, 12, 34]
lst_c.insert(2, 65)
print(f"c = {lst_c}")

# d
lst_d = [43, 12, 12, 34]
# reversed可以讓range(0, len(lst_d))反向進行，
# 避免刪除索引值1的12後，
# 導致後面的索引值都-1，
# 索引值3消失，
# 出現錯誤"Out of range"
for i in reversed(range(0, len(lst_d))):
    if lst_d[i] == 12:
        lst_d.pop(i)
print(f"d = {lst_d}")

# e
lst_e = [43, 12, 12, 34]
lst_e.sort(reverse=False)
print(f" e = {lst_e}")

#f
lst_f = [43, 12, 12, 34]
lst_f.pop()
print(f"f = {lst_f}(先刪除最後一個元素)")
lst_f.pop(2)
print(f"f = {lst_f}(移除索引值2的元素)")


