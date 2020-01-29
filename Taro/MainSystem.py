import Taro.spread.one_card_spread as one
import Taro.spread.three_card_spread as three
import Taro.spread.Celtic_Cross_spread as ccs
import Taro.spread.tree_of_life_card_spread as tree
import Taro.spread.Horse_hoof_spread as horse
import Taro.spread.full_moon_spread as moon

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


if __name__ == "__main__":
    while system.Flag:
        system()
