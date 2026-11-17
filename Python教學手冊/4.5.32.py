nums = [8, 11, 98, 24, 47]

for i in range(0 , len(nums)):
    if(nums[i] % 3 == 0):
        print("包含可被3整除的數")
        break
else:
    print("沒有包含可被3整除的數")
