class Nguoi(object):
    def getGender(self):
        return "Unknow"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nu"
    
aNam = Nam()
aNu = Nu()
print (aNam.getGender())
print (aNu.getGender())
