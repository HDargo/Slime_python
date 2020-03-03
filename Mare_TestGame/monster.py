class monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power


monsters = []


class field_mons_generator:
    def grass_generator(self):
        slime = monster("slime", 5, 10)
        orc = monster("orc", 15, 50)
        goblin = monster("goblin", 20, 20)

        monsters.append(slime)
        monsters.append(orc)
        monsters.append(goblin)

        return monsters
