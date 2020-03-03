from Mare_TestGame.OracleDB import DB


class shop:
    def __init__(self):
        self.WeaponList = DB().WeaponDB()
        self.ArmorList = DB().armorDB()
        self.ItemList = DB().ItemDB()

    def shop(self, pla):
        print("어서옵셔!")
        while True:
            print("[1] 무기를 둘러본다")
            print("[2] 방어구를 둘러본다")
            print("[3] 소비아이템을 둘러본다")
            print("[4] 나간다")
            cho = int(input())
            if cho == 1:
                for a in range(len(self.WeaponList)):
                    print(self.WeaponList[a][1], "공격력 =", self.WeaponList[a][2], "가격 =", self.WeaponList[a][3])
                choice = int(input()) - 1

                if pla.money >= self.WeaponList[choice][3]:
                    pla.money -= self.WeaponList[choice][3]
                    pla.inven += [self.WeaponList[choice]]
                    print("구매완료!")

                elif pla.money < self.WeaponList[choice][3]:
                    print("형씨, 돈이모자라")


            elif cho == 2:
                for a in range(len(self.ArmorList)):
                    print(self.ArmorList[a][1], "방어력 =", self.ArmorList[a][2], "가격 =", self.ArmorList[a][3])
                choice = int(input()) - 1

                if pla.money >= self.ArmorList[choice][3]:
                    pla.money -= self.ArmorList[choice][3]
                    pla.inven += [self.ArmorList[choice]]
                    print("구매완료!")

                elif pla.money < self.ArmorList[choice][3]:
                    print("형씨, 돈이모자라")

            elif cho == 3:
                for a in range(len(self.ItemList)):
                    print(self.ItemList[a][1], self.ItemList[a][2], self.ItemList[a][3], "가격 =", self.ItemList[a][4])
                choice = int(input()) - 1

                if pla.money >= self.ItemList[choice][4]:
                    pla.money -= self.ItemList[choice][4]
                    pla.inven += [self.ItemList[choice]]
                    print("구매완료!")

                elif pla.money < self.ItemList[choice][4]:
                    print("형씨, 돈이모자라")

            elif cho == 4:
                break
