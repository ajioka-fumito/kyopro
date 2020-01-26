s = "3141592653589793238"
ls = [0 for _ in range(10)]

for now in s:
    ls[int(now)]+=1
print(ls)