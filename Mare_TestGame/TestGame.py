from Mare_TestGame.Shop import shop
from Mare_TestGame.Battle import fight
from Mare_TestGame.Player import player


class mainsys:
    def __init__(self):
        self.pla = player()
        self.whatdo()

    def whatdo(self):
        while True:
            try:
                print("무엇을할까?")
                print("[1] 상점가기")
                print("[2] 휴식")
                print("[3] 모험!")
                print("[4] 내상태")
                print("[5] 저장하기")
                do = int(input())

                if do == 1:
                    self.shop()
                elif do == 2:
                    self.heal()
                elif do == 3:
                    self.fight()
                elif do == 4:
                    self.statuspr()
                elif do == 5:
                    self.save()
                else:
                    print("숫자를 잘못 골랐습니다")
            except:
                print("오류 발생 다시입력해주세요")

    def shop(self):
        pass

    def heal(self):
        pass

    def fight(self):
        fight().do(self.pla)

    def statuspr(self):
        print("[1] 상태보기")
        print("[2] 아이템보기")

        choice = int(input())
        if choice == 1:
            self.pla.status()
        if choice == 2:
            self.pla.item()
        self.whatdo()

    def save(self):
        pass


mainsys()


