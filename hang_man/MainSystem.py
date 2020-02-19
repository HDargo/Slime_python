from hang_man.player_word.player import player
from hang_man.player_word.word import wordsel


class hamg_man:

    def __init__(self):
        self.chance = 7
        self.li = player()
        self.question = ""
        self.word = wordsel()  # 랜덤  문자  받기
        self.questionMethod()
        self.li.playerlist(self.word)

    def questionMethod(self):
        for x in range(len(self.word)):
            self.question += "_ "
        print(self.li.answer)
        self.temp()

    def temp(self):
        self.li.check(self.word)
        self.questionMethod()
        while self.chance != 0:
            self.chance -= 1
            pass

    def quest(self):
        pass


if __name__ == "__main__":
    a = hamg_man()
    print(a.word)
    print(a.question)
