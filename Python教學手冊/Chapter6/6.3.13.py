s1 = {3, 2, 2, 1, 4, 5}

print(f"a = {len(s1)}")
print(f"b = {0 in s1}")

s2 = {0,1,2}
print(f"c = {s2 <= s1}")

s3 = set(range(9))
print(f"d = {s3 > s1}")