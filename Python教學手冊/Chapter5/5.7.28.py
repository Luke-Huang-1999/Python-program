def rgb2gray(r,g,b):
    v = int(r * 0.299 + g * 0.587 + b * 0.114)
    return v

print(rgb2gray(100, 120, 100))

lst = [32,56,128]
print(rgb2gray(*lst))


colors = [[34,128,34],[56,22,169],[147,43,98],[155,65,38]]
for i in range(0, len(colors)):
    print(rgb2gray(*colors[i]))