season = ["Spring", "Summer","Autumn","Winter"]
str1 = [season[i][j] for i in range(0, len(season)) for j in range(0, len(season[i])) if season[i][j] in "aeiou"]
print(str1)