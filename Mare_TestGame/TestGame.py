from Mare_TestGame.Shop import shop
from Mare_TestGame.Battle import fight
from Mare_TestGame.Player import player


class mainsys:
    def __init__(self):
        self.pla = player()
        pass

    def shop(self):
        pass

    def heal(self):
        pass

    def fight(self):
        fight()

    def statuspr(self):
        print("[1] 상태보기")
        print("[2] 아이템보기")

        choice = int(input())
        if choice == 1:
            self.pla.status()
        if choice == 2:
            self.pla.item()

    def save(self):
        pass


mainsys().statuspr()


class weapon:
    def __init__(self):
        pass
