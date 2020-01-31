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

    def DescPrint(self, card):
        print(card.Num + "\t" + card.Name)
        print("Upright:\t" + card.Position)
        print("Reversed:\t" + card.R_position)


