class Taro_deck:
    def __init__(self):
        list = []
        list = self.Generator()

    def Generator(self):
        one = Taro_card(1, "The Fool", "Adventure,ignorance", "Frivolity, folly")
        two = Taro_card(2, "	The Magician", "Creation, resourceful", "Timid,deceptio")
        three = Taro_card(3, "The High Priestess", "knowledge", "General")
        four = Taro_card(4, "The Empress", "Pungyang,Motherhood", "Excess, Vanity")
        five = Taro_card(5, "The Empero", "responsibility,")
        six = Taro_card(6, "The Hierophant", "")
        eight = Taro_card(8, "The Chariot", "")
        nine = Taro_card(9, "Strength", "")
        ten = Taro_card(10, "The Hermit", "")
        eleven = Taro_card(11, "Wheel of Fortune", "")
        twelve = Taro_

        return [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
                sixteen, seventeen, eighteen, nineteen, twenty, twenty_one]


class Taro_card:
    def __init__(self, Num):
        self.Num = Num
        self.Name = Name
        self.Position
        self.R_position
