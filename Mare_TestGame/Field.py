import random
from Mare_TestGame.monster import field_mons_generator


class field:
    def __init__(self):
        self.want = 0
        self.fi = "초원"

    def mon(self):
        self.want = int(input())
        if self.want == 1:
            return random.choice(field_mons_generator().grass_generator())
        elif self.want == 2:
            return random.choice(field_mons_generator().forest_generator())

