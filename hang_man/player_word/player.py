import sys
from hang_man.player_word.word import wordsel

class player:

    def __init__(self):
        self.chance = 7
        self.answer = []
        self.word = list(wordsel())

    def playerPlus(self,word_len):
        for x in range(len(word_len)):
            self.answer += "_"

    def check(self, test):
        ans = input()

        if ans in test:
            for x in range(len(test)):

                if ans == self.word[x]:
                    self.answer[x] = self.word[x]
                    self.word[x] = "_"


                    if self.answer.count("_") == 0:
                        print("승리!")
                        sys.exit()

        else:
            print("틀렸습니다")
            self.chance -= 1
            if self.chance == 0:
                print("실패")
                sys.exit()
            print("남은기회:",self.chance)
            self.check(test)





    #플레이어에서 답 입력 함수 실행 후 정답과 비교
    #정답일 시 플레이어 클래스에 있는 정답 리스트에 추가
    #오답일 시 넘어감


