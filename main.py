import random


class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power


class Monster(Character):
    def attack(self, damaged):
        damaged.hp -= random.randint(self.power - 5, self.power + 5)
        if damaged.hp <= 0:
            damaged.hp = 0
            print("monster가 공격으로 {0}을 죽였습니다.".format(damaged.name))
        else:
            print("monster가 {0}을 공격했고, {0}의 hp는 {1}만큼 남았습니다.".format(
                damaged.name, damaged.hp))


class Player(Character):

    def attack(self, damaged):
        damaged.hp -= random.randint(self.power - 5, self.power + 5)
        if damaged.hp <= 0:
            damaged.hp = 0
            print("warrior가 공격으로 {0}을 죽였습니다.".format(damaged.name))
        else:
            print("warrior가 {0}을 공격했고, {0}의 hp는 {1}만큼 남았습니다.".format(
                damaged.name, damaged.hp))

    def magic(self, damaged):
        damaged.hp -= 50
        if damaged.hp <= 0:
            damaged.hp = 0
            print("warrior가 마법공격으로 {0}을 죽였습니다.".format(damaged.name))
        else:
            print("warrior가 {0}을 마법공격했고, {0}의 hp는 {1}만큼 남았습니다.".format(
                damaged.name, damaged.hp))


monster = Monster("monster", 100, 20)
super_monster = Monster("super_monster", 120, 20)
Monsters = [monster, super_monster]

warrior_attack = ["공격", "마법공격"]
warrior = Player("warrior", 200, 20)
magic_count = 2
turn = random.randrange(0, 1)
while True:

    if turn % 2 == 0:

        P_attack = input(f"공격 or 마법공격({str(magic_count)}회 남음):")

        m = random.choice(Monsters)

        if m in Monsters:

            if P_attack == "공격":

                warrior.attack(m)

            elif magic_count > 0 and P_attack == '마법공격':

                warrior.magic(m)

            elif magic_count == 0 and P_attack == '마법공격':
                while "마법공격":
                    print("더이상 마법공격을 할 수 없습니다.")
                    P_attack = input("공격만 가능합니다.")

                    if P_attack == "공격":
                        break
            else:
                while P_attack not in warrior_attack:
                    print("공격과 마법공격 중에 선택하세요.")
                    P_attack = input("공격 or 마법공격:")

                    if P_attack in warrior_attack:
                        break

        if len(Monsters) == 0:
            print('승리')
            break

        if magic_count > 0:
            magic_count -= 1

        else:
            magic_count == 0

    else:
        for m in Monsters:
            choice = random.randrange(0, 1)
            if choice == 0:
                m.attack(warrior)

        if warrior.hp <= 0:
            print('패배')
            break

    turn += 1
