from conDB import Con

c = Con
class Action:
    def selectid(id):
        data = c.selectid(id)
        return data

    def updatehw(ID,status):
        data = c.updatehw(ID,status)
        return data

