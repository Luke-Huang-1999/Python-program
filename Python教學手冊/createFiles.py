chapter = 6
subchapter = 4
start = 16
end = 22

for i in range(start, end + 1):
    filename = f"{chapter}.{subchapter}.{i}.py"

    with open(filename, "w", encoding="utf-8"):
        pass
