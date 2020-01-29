from Taro.spread.one_card_spread import spread as one
from Taro.spread.three_card_spread import spread as three
from Taro.spread.Celtic_Cross_spread import spread as ccs
from Taro.spread.tree_of_life_card_spread import spread as tree
from Taro.spread.Horse_hoof_spread import spread as horse
from Taro.spread.full_moon_spread import spread as moon
from Taro.Taro_Deck.taro_deck import Taro_deck as t

"""

메인 시스템 접속 - 메뉴 출력 - 옵션 선택 - 스프레드 진입

"""


class system:
    Flag = True

    def __init__(self):
        self.spread_list = [one, three, ccs, tree, horse, moon]
        self.OptionPrint()

    def OptionPrint(self):
        print("=====================================================================")
        print("[1] One card spread")
        print("[2] Three card spread")
        print("[3] Celtic cross")
        print("[4] Tree of Life")
        print("[5] Horse hoof")
        print("[6] Full moon")
        print("[7] Exit")
        print("=====================================================================")
        self.Choice()

    def Choice(self):
        num = int(input("Choice : "))
        if num == 7:
            system.Flag = False
        else:
            self.spread(num)

    def spread(self, num):
        spread = self.spread_list[num - 1]
        spread.func1()


if __name__ == "__main__":
    deck = t()
    print(deck.list)
    while system.Flag:
        system()
