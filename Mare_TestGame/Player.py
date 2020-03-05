from Mare_TestGame.Load import Load


class player:
    def __init__(self):

        print("[1]새로운 시작")
        print("[2]이어하기")
        self.new = int(input())
        if self.new == 1:
            print("기본 아이템 지급")
            self.name = input("나의...이름은...")
            self.hp = 100
            self.maxhp = 100
            self.power = 5
            self.armor = 1
            self.money = 30
            self.inven = []
            self.weapon = [[0, "공기", 0, 0]]
            self.clothes = [[1, "공기", 0, 0]]
        elif self.new == 2:
            self.name = Load().Load()["name"]
            self.armor = Load().Load()["armor"]
            self.clothes = Load().Load()["clothes"]
            self.weapon = Load().Load()["weapon"]
            self.maxhp = Load().Load()["maxhp"]
            self.power = Load().Load()["power"]
            self.inven = Load().Load()["inven"]
            self.hp = Load().Load()["hp"]
            self.money = Load().Load()["money"]


    def status(self):
        print("내이름 =", self.name)
        print("현재 체력 =", self.hp)
        print("최대 체력 =", self.maxhp)
        print("공격력 =", self.power)
        print("방어력 =", self.armor)
        print("소지금 =", self.money)
        if self.weapon != ["공기"]:
            print("장비중인 무기 = ", self.weapon)
        elif self.weapon == ["공기"]:
            print("장비중인 무기가 없습니다")
        if self.clothes != ["공기"]:
            print("장비중인 방어구 =", self.clothes)
        elif self.clothes == ["공기"]:
            print("장비중인 방어구가 없습니다.")

    def item(self):
        while True:
            print("[1] 아이템 확인하기")
            print("[2] 장비 착용")
            cho = int(input())
            try:
                if cho == 1:
                    print(self.inven)
                    break
                if cho == 2:
                    print(self.inven)
                    print("장비할 아이템을 골라주십시오")  # TODO
                    choice = int(input()) - 1
                    if self.inven[choice][0] == 0:
                        self.inven += self.weapon
                        self.weapon = []
                        self.weapon += [self.inven[choice]]
                        self.inven.pop(choice)
                        print(self.weapon)
                        break

                    if self.inven[choice][0] == 1:
                        self.inven += self.clothes
                        self.clothes = []
                        self.clothes += [self.inven[choice]]
                        self.inven.pop(choice)
                        print(self.clothes)
                        break
                    if self.inven[choice][0] == 2:
                        print("소비아이템은 장비할수 없습니다")
                        break
            except:
                pass
