import random


class Character:
    def __init__(self, name, max_hp, max_mp, attack_power, magic_power):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mp = max_mp
        self.mp = max_mp
        self.attack_power = attack_power
        self.magic_power = magic_power

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.take_damage(damage)
        print(f"{self.name} 공격했고 {target.name} 에게 {damage}피해를 입혔습니다.")

    def magic_attack(self, target):
        if self.mp < 10:
            print("mp부족")
            return
        damage = random.randint(self.magic_power - 5, self.magic_power + 5)
        self.mp -= 10
        target.take_damage(damage)
        print(f"{self.name} 마법공격을 사용하여 {target.name} 에게 {damage}피해를 입혔습니다.")
        print(f"{self.name} 는 {self.mp} MP남았습니다.")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} 죽었습니다.")
        else:
            print(f"{self.name} 는 {self.hp} hp 남았습니다.")


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 30, 20, 40)


class Monster(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 20, 0)


def battle(player, monster):
    print(f"{monster.name} 나타났습니다")
    while player.hp > 0 and monster.hp > 0:
        print("무슨 공격을 하시겠습니까")
        print("1.공격")
        print("2.마법공격")

        choice = input("선택: ")
        if choice == "1":
            player.attack(monster)
        elif choice == "2":
            player.magic_attack(monster)
        elif choice == "3":
            print("You ran away!")
            return
        else:
            print("1,2 선택")
            continue

        if monster.hp > 0:
            monster.attack(player)

    if player.hp > 0:
        print("승리")
    else:
        print("패배")


player = Player("Player")
monster = Monster("Monster")
battle(player, monster)
