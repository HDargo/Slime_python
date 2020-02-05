class player:

    def __init__(self):
        self.deck = []

    def card_append(self, card):
        self.deck.append(card)
        print(self.deck)


    def card_select(self, next_list_len):


        next_list_len()



    def deck_delete(self):
        le = len(self.deck)
        for a in range(le):
            for b in range(le):
                print("a = ", a)
                print("b = ", b)
                print("le = ", le)
                print("==========")
                if a == b:
                    break
                elif deck[a][1:] == self.deck[b][1:]:
                    print("중복제거")
                    if a > b:
                        self.deck.remove(self.deck[a])
                        self.deck.remove(self.deck[b])
                    if a < b:
                        self.deck.remove(self.deck[b])
                        self.deck.remove(self.deck[a])
                    le -= 2