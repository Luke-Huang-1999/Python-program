country = ["Taiwan","USA","Korea","Japan","Spain","China","UK","French","Switzerland","Danmark"]

print("(a)列出這10個地方：%s\n"%(country))

print("(b)反向列出這10個地方：%s\n"%(country[::-1]))

country.sort()
print("(c)從小排到大列出這10個地方：%s\n"%(country))

country.sort(reverse=True)
print("(d)從大排到小列出這10個地方：%s\n"%(country))

country.insert(0, "Antarctic")
country.append("Arctic Sea")
print("(e)新增資料並列出這12個地方：%s\n"%(country))

cnts = len(country)
HalfCnts = cnts / 2
#print(type(HalfCnts))
country.insert(int(HalfCnts), "Chicago")
print("(f)新增資料在中央位置並列出這13個地方：%s\n"%(country))

country.pop(3)
country.pop(9)
print("(g)刪除第3與第9筆資料並列出這13個地方：%s\n"%(country))






