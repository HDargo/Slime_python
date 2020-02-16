from hang_man.player_word.word import wordsel


class player:
    def __init__(self):
        self.a = wordsel()  # 랜덤  문자  받기

    def question(self):
        question = ""
        for x in range(len(self.a)):
            question += "_"
            question += " "
        return question


a = player()
print(a.a)
print(a.question())
print(a.a)
