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
            print(self.deck.list[int(x)].Name)
        return list(set(num))