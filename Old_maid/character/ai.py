import random


class ai:

    def __init__(self):
        self.deck = []

    def card_append(self, card):
        self.deck.append(card)

    def card_select(self, next_list_len):
        return random.randint(0, next_list_len - 1)

    def deck_delete(self):
        for x in self.deck:
            for z in self.deck:
                if x[1:] == z[1:]:
                    print('AI', self.deck)
                    self.deck.remove(x)
                    self.deck.remove(z)
