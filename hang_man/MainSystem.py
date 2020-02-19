from hang_man.player_word.player import player
from hang_man.player_word.word import wordsel


class hamg_man:

    def __init__(self):
        self.pl = player()
        self.li = player()
        self.question = ""
        self.word = wordsel()  # 랜덤  문자  받기
        self.questionMethod()
        self.li.playerlist(self.word)

    def questionMethod(self):
        for x in range(len(self.word)):
            self.question += "_ "
        print(self.pl.answer)


    def temp(self):
        self.pl.check(self.word)

    def quest(self):
        pass


if __name__ == "__main__":
    a = hamg_man()
    print(a.word)
    print(a.question)
    a.temp()
    a.questionMethod()
