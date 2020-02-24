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
                print("[2] 여관")
                print("[3] 모험!")
                print("[4] 내상태")
                print("[5] 저장하기")
                do = int(input())

                if do == 1:
                    self.shop(self.pla)
                elif do == 2:
                    self.heal(self.pla)
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

    def shop(self,pla):
        shop().shop(self.pla)

    def heal(self,pla):
        print("여관주인:여관은 하룻밤에 10골드야, 뭐 돈없으면...가진돈만 내")
        print("[1] 한숨잔다","[2] 여관을 나간다")
        choice = int(input())
        if choice == 1:
            if pla.money <= 9:
                pla.money = 0
                pla.hp = pla.maxhp
                print("상쾌한 아침! 체력이 모두 회복되었다!...여관주인 아주머니한테 욕먹은거만 빼면")
            else:
                pla.money -= 10
                pla.hp = pla.maxhp
                print("상쾌한 아침! 체력이 모두 회복되었다!")

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


