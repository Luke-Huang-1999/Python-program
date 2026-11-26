chapter = 8
subchapter = 2
start = 8
end = 13

if end > start:
    for i in range(start, end + 1):
        filename = f"{chapter}.{subchapter}.{i}.py"

        with open(filename, "w", encoding="utf-8"):
            pass
