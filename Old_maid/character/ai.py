import random

class ai:

    def __init__(self):
        self.deck = []

    def card_append(self, card):
        self.deck.append(card)

    def card_select(self, next_list_len):
        return random.randint(0, next_list_len - 1)

    def deck_delete(self):
        checkx = 0
        for x in self.deck:
            checkx = checkx + 1
            listx = []
            for y in range(len(self.deck)):
                listx.append(y)
            listx.remove(checkx-1)
            for z in listx:
                if x[1:] == self.deck[z][1:]:
                    self.deck.remove(self.deck[z])
                    self.deck.remove(x)
                    break
        self.deck_check()

    def deck_check(self):
        for x in self.deck:
            checkx = self.deck.index(x)
            listx = []
            for y in range(len(self.deck)):
                listx.append(y)
            listx.remove(checkx)
            for z in listx:
                if x[1:] == self.deck[z][1:]:
                    self.deck_delete()
                    break
