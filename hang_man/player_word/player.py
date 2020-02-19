class player:

    def __init__(self):
        self.answer = []

    def playerlist(self,aaa):
        for x in range(len(aaa)):
            self.answer += ["_"," "]
        print(self.answer)

    def check(self,test):
        ans = input()
        if ans in test:
            print("True")
            for x in range(len(test)):
                print(test[x])

        else:
            print("틀렸습니다")
        pass
    #플레이어에서 답 입력 함수 실행 후 정답과 비교
    #정답일 시 플레이어 클래스에 있는 정답 리스트에 추가
    #오답일 시 넘어감


