from Taro.Taro_Deck.taro_deck import Taro_deck as t


class spread_interface:
    def __init__(self):
        self.deck = t()

    def OptionPrint(self):
        raise NotImplementedError()

    def Generator(self):
        self.deck = t()

    def Optimization(self, dtemp, max):
        num = dtemp.split()
        numc = list(set(num))
        if max == len(num):
            if len(numc) == len(num):
                for x in num:
                    if int(x) >= 21:
                        return "ERROR"
                    if int(x) <= 0:
                        return "ERROR"
                return num
            return "ERROR"
        else:
            return "ERROR"

    def DescPrint(self, num):
        print(self.deck.list[num].Num, "\t", self.deck.list[num].Name)
        print("정방향:\t", self.deck.list[num].Position)
        print("역방향:\t", self.deck.list[num].R_position)
