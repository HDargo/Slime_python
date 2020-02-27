from Mare_TestGame.OracleDB import DB


class shop:
    def shop(self,pla):
        print("어서옵셔!")
        while True:
            print("[1] 상점을 둘러본다")
            print("[2] 나간다")
            cho = int(input())
            if cho == 1:
                print(DB().DB())
                choice = int(input())
                if choice == 1:
                    if pla.money >= 30:
                        pla.money -= 30
                        pla.inven += [DB().DB()[1]]
                        print("구매완료!")
                    elif pla.money < 30:
                        print("형씨, 돈이모자라")

            elif cho == 2:
                break

