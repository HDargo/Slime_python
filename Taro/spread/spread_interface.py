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
        if max == len(num):
            for x in num:
                if int(x) >= 21:
                    return "ERROR"
                if int(x) <= 0:
                    return "ERROR"
            return num
        else:
            return "ERROR"

    def DescPrint(self, card):
        print(card[0]+"\t"+card[1])
        print("Upright:\t"+card[2])
        print("Reversed:\t"+card[3])