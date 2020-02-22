class player:
    def __init__(self):
        self.new = 0
        if self.new == 0:
            print("기본 아이템 지급")
            self.name = input()
            self.hp = 100
            self.maxHp = 100
            self.power = 5
            self.armor = 0
        elif self.new == 1:
            pass

    def status(self):
        print(self.name)
        print(self.hp)
        print(self.maxHp)
        print(self.power)
        print(self.armor)

    def item(self):
        pass
