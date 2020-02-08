import time
import random
from Old_maid.character.ai import ai
from Old_maid.character.player import player

"""

도둑잡기
메인 시스템 - 덱 섞기 - 플레이어 카드 지급 - 인공지능 카드 지급 - 시퀸셜 리스트에 플레이어와 인공지능 순서 결정
게임 시작 전 최대 플레이어 수 결정 최소 3명 최대 8명

조커 한 장을 빼고, 남은 53장의 카드를 전부 나눠 갖는다.

숫자나 글자가 같은 카드가 더 이상 남지 않을 때까지 1쌍씩 버린다.

(반)시계방향으로 상대방의 카드를 한장 가져와서 짝이 맞는 카드가 있으면 버리고 아니면 가지고 있는다. 카드를 전부 버리면 게임에서 빠진다.

3를 반복한다.

마지막으로 조커를 가지고 있는 사람이 패배한다.

"""


class system:
    def __init__(self):
        self.p = player()
        self.playerList = []
        self.deckList = []
        self.flag = True
        self.total = 1

    def GameStart(self):
        playNum = 0
        try:
            print("플레이 할 최대 인공지능 인원 수를 입력하세요 (최소 3명 최대 8명)")
            playNum = int(input("입력 >>>"))

        except ValueError:
            print("숫자를 입력해주세요")
            self.GameStart()
        finally:
            if playNum > 8 or playNum < 3:  # 에러
                print("3명에서 8명 사이로 입력해주세요")
                self.GameStart()
            else:
                self.createObject(playNum)  # 플레이어 및 인공지능 생성
                self.deck_shuffle()  # 덱 생성 및 분배
                self.sequence()

    def sequence(self):
        while self.flag:
            self.playerCheck()
            self.card_select()
            time.sleep(1)

    def card_select(self):
        flag = True
        idx = 0
        le = self.playerList.__len__()
        while flag:
            if self.playerList.__len__() == 1:
                flag = False

            if idx >= le:
                idx = 0

            if idx > le - 1:
                next_card_len = self.playerList[idx + 1].deck.__len__()
                select = self.playerList[idx].card_select(next_card_len)
                next_card = self.playerList[idx + 1].deck.pop(select)
                self.playerList[idx].card_append(next_card)
            else:
                next_card_len = self.playerList[0].deck.__len__()
                select = self.playerList[idx].card_select(next_card_len)
                next_card = self.playerList[0].deck.pop(select)
                self.playerList[idx].card_append(next_card)
            self.playerList[idx].deck_delete()
            for x in self.playerList:
                if x.deck.__len__() == 0:
                    print("남은 사람 = ", le-1)
                    self.playerList.remove(x)
                    le -= 1
            idx += 1

    def playerCheck(self):
        if len(self.playerList) == 1:
            print("게임 종료")
            self.flag = False

    def deck_shuffle(self):
        print("덱 셔플 중...")
        self.deck_generator()
        self.deck_share()
        time.sleep(2)
        print("셔플 완료")

    def deck_generator(self):
        pattern = ["♠", "♣", "♥", "◆"]
        for x in pattern:
            for y in range(1, 14):
                a = ""
                a += x
                if y == 1:
                    a += "A"
                elif y == 11:
                    a += "J"
                elif y == 12:
                    a += "Q"
                elif y == 13:
                    a += "K"
                else:
                    a += str(y)
                self.deckList.append(a)
        self.deckList.append("▶JOKER◀")

    def createObject(self, playNum):
        self.playerList.append(self.p) #테스트로 ai 클래스만으로 실행 # ai클래스가 정상 작동시 주석처리 제거
        for x in range(playNum):
            self.playerList.append(ai())

    def deck_share(self):
        random.shuffle(self.deckList)
        n = 0
        for x in self.deckList:
            self.playerList[n].card_append(x)
            n += 1
            if n == len(self.playerList):
                n = 0
        for x in self.playerList:
            x.deck_delete()


if __name__ == "__main__":
    system().GameStart()
