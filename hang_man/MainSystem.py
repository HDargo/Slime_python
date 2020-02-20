from hang_man.player_word.player import player
from hang_man.player_word.word import wordsel



class hamg_man:

    def __init__(self):
        self.chance = 7
        self.li = player()
        self.question = ""
        self.word = self.li.word  # 랜덤  문자  받기
        self.li.playerPlus(self.word)
        self.questionMethod()
        self.Answer = []

    def questionMethod(self):
        for x in range(len(self.word)):
            self.question += "_ "
        print(self.li.answer)

        self.temp()

    def temp(self):
        self.li.check(self.word)
        self.questionMethod()






if __name__ == "__main__":
    a = hamg_man()
    print(a.word)
    print(a.question)
