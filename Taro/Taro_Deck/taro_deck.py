import random


class Taro_deck:
    def __init__(self):
        self.list = []
        self.list = self.Generator()

    def Generator(self):
        zero = Taro_card(0, "The Fool", "Adventure,ignorance", "Frivolity, folly")
        one = Taro_card(1, "The Magician", "Creation, resourceful", "Timid,deceptio")
        two = Taro_card(2, "The High Priestess", "knowledge", "General")
        three = Taro_card(3, "The Empress", "Pungyang,Motherhood", "Excess, Vanity")
        four = Taro_card(4, "The Empero", "responsibility,Paternity", "arrogance,respect")
        five = Taro_card(5, "The Hierophant", "Teaching, magnanimity", "Narrow,Sloth")
        six = Taro_card(6, "The Lovers", "love, pleasure", "Jealousy, betrayal")
        seven = Taro_card(7, "The Chariot", "Forward,Victory", "Run wild,Frustration")
        eight = Taro_card(8, "Strength", "Strength, courage", "Nature,Conceit")
        nine = Taro_card(9, "The Hermit", "Explore, thoughtful", "shady, closed, avaricious")
        ten = Taro_card(10, "Wheel of Fortune", "opportunity,fortune", "miscalculation,Unfortune")
        eleven = Taro_card(11, "Justice", "Balance,justness", "Prejudice,Denial")
        twelve = Taro_card(12, "The Hanged Man", "Self-sacrifice,Patience", "meaningless sacrifice,Blindness")
        thirteen = Taro_card(13, "Death", "chaos,Parting", "reservation of change,Stuck")
        fourteen = Taro_card(14, "Temperance", " balance,Fruition", "waste, instability")
        fifteen = Taro_card(15, "The Devil", "self-interest, restraint, depravity", "awakening from a vicious circle")
        sixteen = Taro_card(16, "The Tower", "Destruction. Destruction", "Desired destruction")
        seventeen = Taro_card(17, "The Star", "hope, yearning", "disillusionment,Pity")
        eighteen = Taro_card(18, "The Moon", "anxiety, ambiguity, confusion",
                             "relief of anxiety,clarity,he end of chaos")
        nineteen = Taro_card(19, "The Sun", "bright future,Satisfaction", "postpone,failure")
        twenty = Taro_card(20, "Judgement", "Resurrection, improvement", ",regret")
        twenty_one = Taro_card(21, "The world", "Completion,Perfection", "unfinished,uncertain")
        return [zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen,
                fifteen,
                sixteen, seventeen, eighteen, nineteen, twenty, twenty_one]

    def shuffle(self):
        random.shuffle(self.list)

        print("덱을 섞었습니다")


class Taro_card:
    def __init__(self, Num, Name, Position, R_position):
        self.Num = Num
        self.Name = Name
        self.Position = Position
        self.R_position = R_position

if __name__ == "__main__":
    deck = Taro_deck()
    for x in deck.list:
        print(x.Name)
    deck.shuffle()
    for x in deck.list:
        print(x.Name)