from Taro.spread.spread_interface import spread_interface

class spread(spread_interface):
    def OptionPrint(self):
        self.deck.Generator() # 덱 충전
        self.deck.shuffle() # 덱 셔플
        print("=====================================================================")
        print("0 ~ 21 까지의 카드 중 3개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        temp = str(input("Choice : "))
        Opt = self.Optimization(temp)
        if 3 != len(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            pass
