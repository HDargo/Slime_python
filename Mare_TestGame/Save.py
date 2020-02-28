# -*- coding:utf-8 -*-
import json
class Save:
    def __init__(self):
        self.savefile = {}

    def Save(self, pla):
        self.savefile ["name"] = pla.name
        self.savefile["armor"] = pla.armor
        self.savefile["maxhp"] = pla.maxhp
        self.savefile["power"] = pla.power
        self.savefile["money"] = pla.money
        self.savefile["inven"] = pla.inven
        self.savefile["weapon"] = pla.weapon
        self.savefile["clothes"] = pla.clothes
        self.savefile["hp"] = pla.hp
        with open("saveFile.json", "w", encoding="utf-8") as json_file:
            json.dump(self.savefile,json_file)





 #print(self.savefile)
        # save.write(self.savefile)
        # save.close()
        #ctrl + /