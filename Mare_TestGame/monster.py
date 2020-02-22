class  monster:
    def  __init__(self,name,hp,power):
        self.name  = name
        self.hp  = hp
        self.power  = power

monsters  = []
class  field_mons_generator:
    def grasa_generator(self):
        slime  = monster("slime",5,10)
        orc  = monster("orc",30,50)

        monsters.append(slime)
        monsters.append(orc)

        return  monsters