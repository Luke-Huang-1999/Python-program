remove_ne = lambda lst: [lst[i] if (lst[i] >= 0) else 0 for i in range(0, len(lst)) ]
lst = [-3,6,-4,6,8]

print(remove_ne(lst))

#- if 放在 for 後面：篩選元素。
#- if else 放在 for 前面：決定每個元素要放入什麼值。