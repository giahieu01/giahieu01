import math
a=int(input('nhap a: '))
b=int(input('nhap b: '))
c=int(input('nhap c: '))
d=(b*2 - 4*a*c)
if d<0:
    print('phương trinh vo nghiem')
elif d==0:
    x=(-b)/2*a
    print(x)
else:
    x1=((-b)+math.sqrt(d))/2*a
    x2=((-b)-math.sqrt(d))/2*a
    print(x1)
    print(x2)
    
