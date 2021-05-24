def tinh(r):
    chuvi=r*2*3.14
    
    return chuvi
def Tinh(h):
    dientich=h*h*3.14
    return dientich
   
r=int(input())
h=int(input())
if r>0:
    print('r la ban kinh')
else:
    print('r k la ban kinh')

p= tinh(r)
s=Tinh(h)
print(p)
print(s)

