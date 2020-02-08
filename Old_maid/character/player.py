class player:

    def __init__(self):
        self.deck = []

    def card_append(self, card):
        self.deck.append(card)
        print(self.deck)

    def card_select(self, next_list_len):
        if next_list_len == 1:
            return 0
        while True:
            try:
                print("뽑을  카드를  골라주세요")
                for x in range(next_list_len):
                    print(x + 1, end=" ")
                print()
                pl = int(input())
                if pl < 0 or pl > next_list_len:
                    pass
                return pl - 1
            except:
                print("오류가 발생했습니다 숫자를 다시 골라주세요")

    def deck_delete(self):
        try:
            y = 0
            le = len(self.deck)
            for a in range(le):
                x = 0
                y += 1
                for b in range(le):
                    x += 1
                    if self.deck[x - 1] == self.deck[y - 1]:
                        continue
                    if y - 1 >= le:
                        y = 0
                    if x - 1 >= le:
                        x = 0
                    elif self.deck[x - 1][1:] == self.deck[y - 1][1:]:
                        if x - 1 > y - 1:
                            self.deck.remove(self.deck[x - 1])
                            self.deck.remove(self.deck[y - 1])
                        if x - 1 < y - 1:
                            self.deck.remove(self.deck[y - 1])
                            self.deck.remove(self.deck[x - 1])
                        x = 0
                        y = 0
                        le -= 2
        except:
            print("끝")
