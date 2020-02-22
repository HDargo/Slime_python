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
            self.power = 1
            self.armor = 100
            self.money = 50
            self.inven = ["시작의 검","허름한 가죽옷","빨간포션"]
        elif self.new == 2:
            pass


    def status(self):
        print("내이름 =",self.name)
        print("현재 체력 =",self.hp)
        print("최대 체력 =",self.maxhp)
        print("공격력 =",self.power)
        print("방어력 =",self.armor)
        print("소지금 =",self.money)

    def item(self):
        print(self.inven)
