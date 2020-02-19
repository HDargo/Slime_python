import sys

class player:

    def __init__(self):
        self.chance = 7
        self.answer = []

    def playerlist(self,word_len):
        for x in range(len(word_len)):
            self.answer.append("_")
        print(self.answer)

    def check(self,test):
        ans = input()

        if ans in test:
            for x in range(len(test)):
                print(test[x])
        if self.chance == 0:
            print("실패")
            sys.exit


        else:
            print("틀렸습니다")
            self.chance -= 1
            print(self.chance)
            self.check(test)

    #플레이어에서 답 입력 함수 실행 후 정답과 비교
    #정답일 시 플레이어 클래스에 있는 정답 리스트에 추가
    #오답일 시 넘어감


