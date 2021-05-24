p=tuple()
for i in range (2,1000):
    dem=0
    for j in range(1, i+1):
        if(i%j==0):
            dem=dem+1
    if(dem==2):
        p = p +(i,)
print(p)
