
class Save:
    def Save(self,pla):
        self.savefile = []
        self.savefile += [pla.name,pla.hp,pla.maxhp,pla.power,pla.armor,pla.money,pla.inven,pla.weapon,pla.clothes]
        print(22222)
        save = open("세이브.txt", "w")
        print(self.savefile)
        save.write(str(self.savefile))
        save.close()