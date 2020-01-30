from Taro.Taro_Deck.taro_deck import Taro_deck as t


class spread_interface:
    def __init__(self):
        self.deck = t()

    def OptionPrint(self):
        raise NotImplementedError()

    def Generator(self):
        self.deck = t()

    def Optimization(self,dtemp):
        num = dtemp.split()
        for x in list(set(num)):
            if int(x) < 22:
                pass
            else:
                return "ERROR"
        return list(set(num))