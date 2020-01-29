from Taro.Taro_Deck.taro_deck import Taro_deck as t


class spread_interface:
    def __init__(self):
        self.deck = t()

    def func1(self):
        raise NotImplementedError()

    def func2(self):
        raise NotImplementedError()
