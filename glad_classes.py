import random
from sys import exit
import glad_global_info as info
import glad_items as items
import glad_inventory as inventory


class Contestant(inventory.Person):
    def __init__(self, name, pl_controlled, skill, speed, strength):
        super().__init__(name, pl_controlled, 15, 0, 0, 0, 0)
        self.skill = skill
        self.speed = speed
        self.strength = strength
        self.health = 10
        self.weapon = None
        self.defense = 0
        self.armor = None
    #: Effectively the battle forumla.
    def getDamage(self):
        return float((self.strength + self.weapon.damage)/2)
    def getSpeed(self):
        return float(((self.speed + self.weapon.speed)/2) - (self.armor.weight)/4)
    def getDefense(self):
        self.defense = float(self.armor.defense/3.25)
    def takeDamage(self,damage):
        self.health -= damage
    def increaseHealth(self, health_incr):
        self.health += health_incr
    def increaseStrength(self, strength_incr):
        self.strength += strength_incr
    def increaseDefense(self, defense_incr):
        self.armor.defense += defense_incr
    def increaseSpeed(self, speed_incr):
        self.speed += speed_incr

class Stats():
    def __init__(self, skill, speed, damage, health):
        self.skill = skill
        self.speed = speed
        self.damage = damage
        self.health = health

#: without setting player.name to pl_name here, player.name doesn't update.
def get_player_name():
    info.pl_name = input("\nWhat is your name?\n> ")
    info.player.name = info.pl_name
    info.health_reset = info.player.health
    info.strength_reset = info.player.strength
    info.defense_reset = info.player.defense
    info.speed_reset = info.player.speed
