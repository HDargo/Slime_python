from Mare_TestGame.Field import field

class fight:
    def __init__(self):
        self.mon = None

    def do(self):
        print("어디로 갈까?")
        print("필드 종류")
        print("[1] 초원")
        self.mon = field().mon()
        print("야생의", self.mon.name, "와(과) 조우했다!", "체력 =", self.mon.hp, "공격력 = ", self.mon.power)



    def battle(self):
        print("가능한 행동")
        print("[1] 공격한다","[2] 방어한다","[3] 아이템 사용","[4]튄다")
        whatdo = input()
        if whatdo == 1:
            pass
        if whatdo == 2:
            pass
        if whatdo == 3:
            pass
        if whatdo == 4:
            pass
        else:
            print("다시골라 주십시오")
            self.battle()

    def reward(self):
        pass


fight()
