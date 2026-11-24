chapter = 7
subchapter = 2
start = 6
end = 12

for i in range(start, end + 1):
    filename = f"{chapter}.{subchapter}.{i}.py"

    with open(filename, "w", encoding="utf-8"):
        pass
