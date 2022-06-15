from conDB import Con

c = Con
class Action:
    def selectid(ID):
        data = c.selectid(ID)
        return data

    def updatehw(ID,status):
        t = c.updatehw(ID,status)
        if (t==True):
            data = c.selectid(ID)
        else:
            data = {"error",True}
        return data

    def inserthw(name,hw_name):
        ID = c.inserthw(name,hw_name)
        if(ID):
            data = c.selectid(ID)
        else:
            data = {"error",True}
        return data

