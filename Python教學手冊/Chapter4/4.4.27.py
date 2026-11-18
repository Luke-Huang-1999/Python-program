i = 1
a = []
max = 3
while i <= 100:
    if(i % 3 == 2):
        if(i % 5 == 3):
            if(i % 7 == 2):
                a.append(i)
                if len(a) >= max:
                    break
    i +=1

#print(f"這群學生最少有{i}人")
print(f"有可能有{a}人")
