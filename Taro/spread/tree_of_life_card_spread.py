from Taro.spread.spread_interface import spread_interface


class spread(spread_interface):
    def OptionPrint(self):
        print("=====================================================================")
        print("생명의 나무 스프레드")
        print("0 ~ 21 까지의 카드 중 10개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        TreeDesc = ["1. \t 영적인 것",
                    "2. \t 책임",
                    "3. \t 장애물",
                    "4. \t 도움을 주는 것",
                    "5. \t 나를 반대하는 것, 혹은 문제가 되는 것.",
                    "6. \t 성취할 수 있는 것.",
                    "7. \t 감정 관계",
                    "8. \t 인간관계 및 커리어",
                    "9. \t 무의식의 기반",
                    "10. \t 가족들에 대해."]
        temp = input("Choice : ")
        Opt = self.Optimization(temp, 10)
        if list != type(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            for x in range(len(Opt)):
                print(TreeDesc[x])
                self.DescPrint(int(x))