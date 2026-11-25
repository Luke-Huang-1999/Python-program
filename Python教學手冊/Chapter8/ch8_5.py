with open("temperture.txt", "w", encoding="utf-8") as f:
    f.writelines(["星期一 18 25\n", "星期二 20 27\n", "星期三 19 26\n"])

with open("temperture.txt", "r", encoding="utf-8") as f:
    #Python 的檔案物件在迭代（Iteration）時，預設以「一行」作為一次迭代的單位。
    temps = [line.split() for line in f]
print(temps)

for day ,t1,t2 in temps:
    avg_temp = (int(t1) + int(t2))/2
    print(f"{day}的平均溫度：{avg_temp:.1f}度")