lst = [12, 43, 83, 91]
a = lst

print(f"lst = {lst}, 記憶體位址 = {id(lst)}")
print(f"a = {a}, 記憶體位址 = {id(a)}")

a.append(23)
print("append之後")

print(f"lst = {lst}, 記憶體位址 = {id(lst)}")
print(f"a = {a}, 記憶體位址 = {id(a)}")

#lst這個變數實際存的是[12, 43, 83, 91]的記憶體位址
#a = lst會將lst存的記憶體位址複製一份給a
#所以a.apppend(23)會連同lst一起被影響，因為都是在看同一個物件[12, 43, 83, 91]