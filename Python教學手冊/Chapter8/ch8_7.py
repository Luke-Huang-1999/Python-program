matrix = [[12, 34, 56, 78], [90, 23, 45, 67], [89, 21, 43, 65]]

with open("matrix.bin","wb") as file:
    for row in matrix:
        file.write(bytes(row))

r_matrix = []
with open("matrix.bin","rb") as file:
    for _ in range(0, 3):
        row = list(file.read(4))
        r_matrix.append(row)
        print(row)