import random
from sys import exit
import glad_global_info as info
import glad_items as items
import glad_inventory as inventory


class Contestant(inventory.Person):
    def __init__(self, name, pl_controlled, skill, speed, strength, gold, potion, sweetcakes):
        super().__init__(name, pl_controlled, gold, potion, sweetcakes)
        self.skill = skill
        self.speed = speed
        self.strength = strength
        self.health = 10
        self.weapon = None
        self.armor = None
    #: Effectively the battle forumla.
    def getDamage(self):
        return float((self.strength + self.weapon.damage)/2)
    def getSpeed(self):
        return float(((self.speed + self.weapon.speed)/2) - (self.armor.defense)/4)
    def getDefense(self):
        return float(self.armor.defense/4)
    def takeDamage(self,damage):
        self.health -= damage
    def healUser(self, heal):
        self.health += heal_amount

class Stats():
    def __init__(self, skill, speed, damage, health):
        self.skill = skill
        self.speed = speed
        self.damage = damage
        self.health = health

#: without setting player.name to pl_name here, player.name doesn't update.
def get_player_name():
    info.pl_name = input("What is your name?\n> ")
    info.player.name = info.pl_name
    info.start_health = info.player.health
