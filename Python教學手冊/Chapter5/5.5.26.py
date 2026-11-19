lst = [-3, 6, 100, 300]

find_inrange = lambda lst:[lst[i] for i in range(0, len(lst)) if 0 <= lst[i] <= 255]

print(find_inrange(lst))