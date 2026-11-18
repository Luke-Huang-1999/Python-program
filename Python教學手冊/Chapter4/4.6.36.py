str1 = ["State", "University", "of", "New", "York", "at", "Buffalo"]
result = [str1[i] for i in range(0, len(str1)) for j in range(0, len(str1[i])) if str1[i][j] in 'a']
print(result)