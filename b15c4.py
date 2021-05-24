s=input('Nhap tu vao: ').split()
s.sort()
b=len(s)
print(s)
s1=range(0,b)
c=zip(s,s1)
for i in c:
    print(i)