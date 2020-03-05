from Mare_TestGame.OracleDB import DB

class monster:
    def __init__(self, name, hp, power, reward):
        self.name = name
        self.hp = hp
        self.power = power
        self.reward = reward


monsters = []


class field_mons_generator:
    def grass_generator(self):
        monsters = []
        slime = monster("슬라임", 5, 10, 5)
        orc = monster("오크", 15, 50, 50)
        goblin = monster("고블린", 20, 20, 15)
        kingslime = monster("킹슬라임", 200, 30, 100)

        for a in range(5):
            monsters.append(slime)
        for a in range(2):
            monsters.append(orc)
        for a in range(3):
            monsters.append(goblin)

        monsters.append(kingslime)

        return monsters

    def forest_generator(self):
        monsters = []
        troll = monster("트롤", 30, 20, 25)
        wolf = monster("늑대", 25, 25, 20)

        for a in range(3):
            monsters.append(troll)
        for a in range(2):
            monsters.append(wolf)

        return monsters
