from Taro.spread.spread_interface import spread_interface


class spread(spread_interface):
    def OptionPrint(self):
        super().Generator()
        print("=====================================================================")
        print("0 ~ 21 까지의 카드 중 1개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        num = int(input("Choice : "))
        print(self.deck[num].Name)
