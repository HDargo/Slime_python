from Mare_TestGame.Field import field
import time

class fight:
    def __init__(self):
        self.mon = None

    def do(self,pla):
        print("어디로 갈까?")
        print("필드 종류")
        print("[1] 초원")
        self.mon = field().mon()
        print("야생의", self.mon.name, "와(과) 조우했다!", "체력 =", self.mon.hp, "공격력 = ", self.mon.power)
        self.battle(pla)



    def battle(self,pla):
        while True:
            if pla.hp <= 0:
                print("일단 정신 똑바로 차리고...도망쳐!")
                pla.hp = 1
                break
            elif self.mon.hp <= 0:
                print("승리!")
                self.reward(pla)
                break

            print("가능한 행동")
            print("[1] 공격한다","[2] 방어한다","[3] 아이템 사용","[4]튄다")
            print(pla.maxhp,"/",pla.hp,"내 공격력 =",pla.power,"내 방어력 =",pla.armor)
            print(self.mon.name,"의 남은 체력",self.mon.hp)
            whatdo = int(input())

            if whatdo == 1:
                self.mon.hp -= pla.power + pla.weapon[0][2]
                print(self.mon.name,"에게",pla.power + pla.weapon[0][2],"만큼의 피해를 입혔다!")
                time.sleep(1)
                if pla.armor + pla.clothes[0][2] >= self.mon.power:
                    print("이 적은 당신에게 피해를 입히기엔 너무 약하다")
                    time.sleep(1)
                else:
                    damage = self.mon.power - (pla.armor + pla.clothes[0][2] )
                    pla.hp -= damage
                    print("적에게",damage,"만큼의 피해를 입었다")
                    time.sleep(1)

            elif whatdo == 2:
                shild = (pla.armor + pla.clothes[0][2])*2
                if shild > self.mon.power:
                    print("적절한 방어!")
                else:
                    damage = self.mon.power - shild
                    pla.hp -= damage
                    print("막았음애도 불구하고",damage,"만큼의 피해를 입었다!")
            elif whatdo == 3:
                print(pla.inven)
                print("무엇을 쓸까?")
                cho = int(input()) - 1
                if pla.inven[cho][0] == 2:
                    if pla.hp + pla.inven[cho][2] < pla.maxhp:
                        pla.hp += pla.inven[cho][2]
                        print(pla.inven[cho][2],"만큼 회복해서","체력이",pla.hp,"이 되었다!")
                    elif pla.hp +pla.inven[cho][2] >= pla.maxhp:
                        pla.hp = pla.maxhp
                        print("완전히 회복했다!")
                    if pla.armor + pla.clothes[0][2] >= self.mon.power:
                        print("이 적은 당신에게 피해를 입히기엔 너무 약하다")
                        time.sleep(1)
                    else:
                        damage = self.mon.power - (pla.armor + pla.clothes[0][2])
                        pla.hp -= damage
                        print("적에게", damage, "만큼의 피해를 입었다")
                        time.sleep(1)
                elif pla.inven[cho][0] != 2:
                    print("전투 중에는 소비 아이템만 사용할수 있습니다")

            elif whatdo == 4:
                print("작전상 후퇴다!")
                break
            else:
                print("다시골라 주십시오")


    def reward(self,pla):
        print("10골드 획득!")
        pla.money += 10
        time.sleep(2)



fight()
