chapter = 8
subchapter = 1
start = 1
end = 7

if end > start and end > (start * 2):
    for i in range(start, end + 1):
        filename = f"{chapter}.{subchapter}.{i}.py"

        with open(filename, "w", encoding="utf-8"):
            pass
