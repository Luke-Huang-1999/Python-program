import csv

lst = [["John", 18, 85], ["Mary", 19, 90], ["Jeff", 17, 78]]
with open("ex8_6.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["姓名", "年齡", "成績"])
    writer.writerows(lst)


with open("ex8_6.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    next(reader)
    for name, age, score in reader:
        print(f"姓名：{name}, 年齡：{age}, 成績：{score}")