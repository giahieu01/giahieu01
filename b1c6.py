class Cricle(object):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2*3.14
r=int(input("nhap ban kinh:"))
c=Cricle(r)
print("dien tich hinh tron la:",c.area())      
