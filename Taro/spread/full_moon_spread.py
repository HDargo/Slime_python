from Taro.spread.spread_interface import spread_interface


class spread(spread_interface):
    def OptionPrint(self):
        print("=====================================================================")
        print("보름달 스프레드")
        print("0 ~ 21 까지의 카드 중 7개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        MoonDesc = [
            "1. \t 질문자의 지금 삶",
            "2. \t 인간관계 및 주변 환경",
            "3. \t 목표를 방해하는 것",
            "4. \t 장애물을 극복하기 위해서는 어떻게 해야 하나?",
            "5. \t 목표를 이루기 위해 질문자가 해야할 것",
            "6. \t 목표를 위하여 외부, 혹은 타인으로부터 배워야 할 것.",
            "7. \t 예상 결과"]
        temp = input("Choice : ")
        Opt = self.Optimization(temp, 7)
        if list != type(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            for x in range(len(Opt)):
                print(MoonDesc[x])
                self.DescPrint(int(x))