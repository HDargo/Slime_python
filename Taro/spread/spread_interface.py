from Taro.Taro_Deck import taro_deck


class spread_interface:
    def __init__(self):
        self.deck = taro_deck.Taro_deck

    def func1(self):
        raise NotImplementedError()

    def func2(self):
        raise NotImplementedError()
