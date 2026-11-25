file = open("demo.txt", "w", encoding="utf-8")

file.write("天青色等煙雨，")
file.write("而我在等妳。\n")

file.writelines(["月色被打撈起，", "暈開了結局。\n"])
file.close()