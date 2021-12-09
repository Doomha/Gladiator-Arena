import random
from sys import exit
import glad_global_info as info

class Weapon:
    def __init__(self, name, w_type, speed, damage):
        self.name = name
        self.w_type = w_type
        self.speed = speed
        self.damage = damage

class Ranged_weapon(Weapon):
    def __init__(self, name, speed, damage, w_range):
        super().__init__(name, "ranged", speed, damage)
        self.w_range = w_range

class Bow(Ranged_weapon):
    def __init__(self):
        super().__init__("Bow", 5, 5, 8)

class Melee_weapon(Weapon):
    def __init__(self, name, speed, damage, w_power):
        super().__init__(name, "melee", speed, damage)
        self.w_power = w_power

class Sword(Melee_weapon):
    def __init__(self):
        super().__init__("Sword", 4, 7, 5)

class Spear(Melee_weapon):
    def __init__(self):
        super().__init__("Spear", 6, 4, 3)

class Rock(Melee_weapon):
    def __init__(self):
        super().__init__("Rock", 1, 1, 1)

class Magic_weapon(Weapon):
    def __init__(self, name, speed, damage, power):
        super().__init__(name, speed, damage)
        self.power = power

class Armor:
    def __init__(self, name, defense, weight):
        self.name = name
        self.defense = defense
        self.weight = weight

class Magic_armor(Armor):
    def __init__(self, name, defense, weight, a_magic_buff):
        super().__init__(name, defense, weight)
        self.a_magic_buff = a_magic_buff

class Contestant:
    def __init__(self, name, skill, speed, strength):
        self.name = name
        self.skill = skill
        self.speed = speed
        self.strength = strength
        self.health = 10
        self.weapon = None
    #: Effectively the battle forumla.
    def getDamage(self):
        return float((self.strength + self.weapon.damage)/2)
    def getSpeed(self):
        return float((self.speed + self.weapon.speed)/2)
    def takeDamage(self,damage):
        self.health -= damage

class Stats:
    def __init__(self, skill, speed, damage, health):
        self.skill = skill
        self.speed = speed
        self.damage = damage
        self.health = health

def get_player_name():
    info.pl_name = input("What is your name?\n> ")
    print(info.pl_name)
    print(info.player.name)
