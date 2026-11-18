def find_max(*num):
    max = num[0]
    for i in range(0, len(num)):
        if max < num[i]:
            max = num[i]
    return max


print(find_max(4, 9, 3))
print(find_max(6, 4))
