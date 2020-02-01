import random


class Taro_deck:
    def __init__(self):
        self.list = self.Generator()

    def Generator(self):
        zero = Taro_card(0, "The Fool", "모험, 무지", "경솔, 어리석음")
        one = Taro_card(1, "The Magician", "창조, 수완", "겁많음, 기만")
        two = Taro_card(2, "The High Priestess", "지식, 총명","잔혹, 무례함")
        three = Taro_card(3, "The Empress", "풍양, 모성", "과잉, 허영")
        four = Taro_card(4, "The Empero", "책임, 부성", "오만, 존대")
        five = Taro_card(5, "The Hierophant", "가르침, 관대함", "협량, 나태")
        six = Taro_card(6, "The Lovers", "연애, 쾌락", "질투, 배신")
        seven = Taro_card(7, "The Chariot", "전진, 승리", "폭주, 좌절")
        eight = Taro_card(8, "Strength", "힘, 용기", "본성, 자만")
        nine = Taro_card(9, "The Hermit", "탐색, 사려깊음", "음습, 폐쇄적, 탐욕")
        ten = Taro_card(10, "Wheel of Fortune", "기회, 일시적인 행운", "오산, 불운")
        eleven = Taro_card(11, "Justice", "균형, 정당함", "편견, 부정")
        twelve = Taro_card(12, "The Hanged Man", "자기희생, 인내", "무의미한 희생, 맹목")
        thirteen = Taro_card(13, "Death", "격변, 이별", "변화의 유보, 고착")
        fourteen = Taro_card(14, "Temperance", " 조화, 견실", "낭비, 불안정")
        fifteen = Taro_card(15, "The Devil", "사심, 속박, 타락", "악순환으로부터의 각성")
        sixteen = Taro_card(16, "The Tower", "파괴, 파멸", "필요로 하는 파괴")
        seventeen = Taro_card(17, "The Star", "희망, 동경", "환멸, 비애")
        eighteen = Taro_card(18, "The Moon", "불안, 애매함, 혼돈","불안 해소, 명료함, 혼돈의 끝")
        nineteen = Taro_card(19, "The Sun", "밝은 미래, 만족", "연기,실패")
        twenty = Taro_card(20, "Judgement", "부활, 개선", ",재기불능, 후회")
        twenty_one = Taro_card(21, "The world", "완성, 완전", "미완성, 어중간함")
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

