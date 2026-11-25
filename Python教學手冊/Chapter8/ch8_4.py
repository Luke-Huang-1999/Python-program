with open("text.txt", "w", encoding="utf-8") as f:
    f.write("Python程式設計")

with open("text.txt", "r", encoding="utf-8") as f:
    print(f"讀取兩個字元：{f.read(2)}")
    print(f"指標位置：{f.tell()}")
    print(f"讀取六個字元：{f.read(6)}")
    print(f"指標位置：{f.tell()}")
    f.seek(0)
    print(f"從頭到尾讀取檔案所有內容：{f.read()}")