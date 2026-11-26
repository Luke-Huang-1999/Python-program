import pickle

lst = [2]

for i in range(3, 1000):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        lst.append(i)

print(lst)

with open("ex8_4.bin", "wb") as file:
    pickle.dump(lst, file)

with open("ex8_4.bin", "rb") as file:
    loaded_data = pickle.load(file)
print(loaded_data)
