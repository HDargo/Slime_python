from Taro.spread.one_card_spread import spread as one
from Taro.spread.three_card_spread import spread as three
from Taro.spread.Celtic_Cross_spread import spread as ccs
from Taro.spread.tree_of_life_card_spread import spread as tree
from Taro.spread.Horse_hoof_spread import spread as horse
from Taro.spread.full_moon_spread import spread as moon


class system:
    Flag = True

    def __init__(self):
        self.spread_list = [one(), three(), ccs(), tree(), horse(), moon()]
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
        try:
            num = int(input("Choice : "))
            if num == 7:
                system.Flag = False
            else:
                self.spread(num)
        except ValueError:
            print("숫자를 입력해주세요")
            self.OptionPrint()

    def spread(self, num):
        self.spread_list[num - 1].OptionPrint()  # run spread


if __name__ == "__main__":
    while system.Flag:
        system()
