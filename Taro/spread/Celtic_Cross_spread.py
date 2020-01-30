from Taro.spread.spread_interface import spread_interface


class spread(spread_interface):
    def OptionPrint(self):
        self.deck.Generator()
        self.deck.shuffle()
        CelticDesc = [
            "1.\tNow: 현재 처한 상황.",
            "2.\tChallenge: 방해하는 것, 혹은 영향을 행사하는 것.",
            "3.\tPast: 먼 과거.",
            "4.\tRecent past: 질문자에게 영향을 끼칠 수 있는 가까운 과거. 혹은 얽매여 있는 과거의 사념.",
            "5.\tFuture: 직면하고 있는 가까운 미래.",
            "6.\tOutcome: 아무런 대응을 하지 않을 때의 결과. 5번에 대한 일반적인 해답.",
            "7.\tYou: 현재 질문자의 심리와 감정. 1번 카드와 가장 밀접한 관계가 있으며, 조금 더 명백한 내면을 투사한다.",
            "8.\tExternal: 외부 요인. 타인의 영향력, 혹은 타인이 이 문제를 바라보는 시각.",
            "9.\tHopes and Desires: 희망 혹은 두려움.",
            "10.\tFinal outcome: 문제의 총체적 해결. 모든 카드들을 아울러 미래적 시각으로 해석."]
        print("=====================================================================")
        print("0 ~ 21 까지의 카드 중 10개를 선택 해 주세요.")
        print("그 외 숫자를 입력하시면 취소됩니다")
        print("=====================================================================")
        temp = input("Choice : ")
        Opt = self.Optimization(temp)
        if list != type(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            pass
        if 10 != len(Opt):
            print("오류!")
            self.OptionPrint()
        else:
            pass

        for x in range(10):
            print(CelticDesc[x])
            DescPrint(deck[opt[x]])