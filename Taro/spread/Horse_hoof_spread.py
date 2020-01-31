from Taro.spread.spread_interface import spread_interface


class spread(spread_interface):
    def OptionPrint(self):
        self.deck.Generator()
        self.deck.shuffle()
        HorseDesc = [
            "1. \t 질문자의 현재 ",
            "2. \t 질문자가 나아가야 할 방향",
            "3. \t 장애물",
            "4. \t 힘을 주는것과 일을 해쳐나갈 지략",
            "5. \t 결과"]
        print("=====================================================================")
        print("0 ~ 21 까지의 카드 중 1개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        num = int(input("Choice : "))
        print(self.deck.list[num].Name)
        temp = input("Choice : ")
        Opt = self.Optimization(temp)
        if list != type(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            pass
        if 5 != len(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            pass

        for x in range(5):
            print(HorseDesc[x])
            self.DescPrint(self.deck[Opt[x]])