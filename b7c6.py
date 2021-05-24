class Cricle(object):
    def __init__(self,r):
        self.r=r
    def chu_vi(self):
        return 2*self.r*3.14
    def dien_tich(self):
        return self.r**2*3.14
r=int(input("nhap ban kinh:"))
c=Cricle(r)
print("chu vi hinh tron la:",c.chu_vi())
print("dien tich hinh tron la:",c.dien_tich())
