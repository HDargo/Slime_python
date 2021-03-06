from Taro.spread.spread_interface import spread_interface

class spread(spread_interface):
    def OptionPrint(self):
        self.deck.Generator()  # 덱 충전
        self.deck.shuffle()  # 덱 셔플
        print("=====================================================================")
        print("0 ~ 21 까지의 카드 중 3개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        ThreeDesc = ["1. \t 과거",
                     "2. \t 현재",
                     "3. \t 미래"]
        temp = input("Choice : ")
        Opt = self.Optimization(temp, 3)
        if list != type(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            for x in range(len(Opt)):
                print(ThreeDesc[x])
                self.DescPrint(int(x))