import random
from Mare_TestGame.monster import field_mons_generator


class field:
    def __init__(self):
        print("어디로 갈까?")
        print("필드 종류")
        print("[1] 초원")
        self.want = 0
        self.fi = "초원"

    def mon(self):
        self.want = int(input())
        if self.want == 1:
            return random.choice(field_mons_generator().grasa_generator())

    def reward(self):
        pass


f = field()
mon = f.mon()
print(mon.name,mon.hp,mon.power)
