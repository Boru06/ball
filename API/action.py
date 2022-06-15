from conDB import Con

c = Con
class Action:
    def gethw():
        data = c.gethw()
        return data

x = Action.gethw()
print(x)