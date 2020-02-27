class player:
    def __init__(self):
        print("[1]새로운 시작")
        print("[2]이어하기")
        self.new = int(input())
        if self.new == 1:
            print("기본 아이템 지급")
            self.name = input("나의...이름은...")
            self.hp = 50
            self.maxhp = 100
            self.power = 5
            self.armor = 2
            self.money = 1
            self.inven = []
            self.weapon = []
            self.clothes = []
        elif self.new == 2:
            pass


    def status(self):
        print("내이름 =",self.name)
        print("현재 체력 =",self.hp)
        print("최대 체력 =",self.maxhp)
        print("공격력 =",self.power)
        print("방어력 =",self.armor)
        print("소지금 =",self.money)
        if self.weapon != []:
            print("장비중인 무기 = ",self.weapon)
        elif self.weapon == []:
            print("장비중인 무기가 없습니다")
        if self.clothes != []:
            print("장비중인 방어구 =",self.clothes)
        elif self.clothes == []:
            print("장비중인 방어구가 없습니다.")

    def item(self):
        print(self.inven)


