chapter = 6
subchapter = 3
start = 11
end = 15

for i in range(start, end + 1):
    filename = f"{chapter}.{subchapter}.{i}.py"

    with open(filename, "w", encoding="utf-8"):
        pass
