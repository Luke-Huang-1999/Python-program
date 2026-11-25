file = open("demo.txt", "a", encoding="utf-8")

file.write("如傳世的青花瓷自顧自美麗，\n")
file.write("你帶著笑意。\n")

file.close()

file = open("demo.txt", "r", encoding="utf-8")
print(file.read())
file.close()