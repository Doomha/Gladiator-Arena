import random
from sys import exit
import glad_global_info as info
import glad_items as items
import glad_inventory as inventory


class Contestant(inventory.Person):
    def __init__(self, name, pl_controlled):
        super().__init__(name, pl_controlled, 15, 0, 0, 0, 0)
        self.skill = 0
        self.speed = 0
        self.strength = 0
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

    def fight_aggressive(self):
        self.defense -= (self.defense * 0.5)
        self.speed += (self.speed * 0.2)
        self.strength += (self.strength * 0.2)
        self.zero_stat_check()
        if self.pl_controlled == True:
            pl_attack = "aggressively"
        else:
            oppo_attack = "aggressively"
    def fight_conservative(self):
        self.defense += (self.defense * 0.5)
        self.speed -= (self.speed * 0.2)
        self.strength -= (self.strength * 0.2)
        self.zero_stat_check()
        if self.pl_controlled == True:
            pl_attack = "conservatively"
        else:
            oppo_attack = "conservatively"

    def zero_stat_check(self):
        if self.defense < 0:
            self.defense = 0
        if self.speed < 0:
            self.speed = 0
        if self.strength < 0:
            self.strength = 0

    def get_aggression(self):
        cons = "conservatively"
        norm = "normally"
        aggr = "aggressively"
        if self.pl_controlled == False:
            if info.game_mode.mode_name == "Easy":
                self.fight_conservative()
                info.oppo_attack = cons
            elif info.game_mode.mode_name == "Normal":
                d = random.randrange(4)
                if d == 1:
                    self.fight_conservative()
                    info.oppo_attack = cons
                elif d == 2:
                    info.oppo_attack = norm
                else:
                    self.fight_aggressive()
                    info.oppo_attack = aggr
            elif info.game_mode.mode_name == "Hard":
                if self.health >= 4:
                    self.fight_aggressive()
                    info.oppo_attack = aggr
                elif info.player.health > (self.health - 4):
                    self.fight_aggressive()
                    info.oppo_attack = aggr
                elif self.health > (info.player.health - 5):
                    self.fight_conservative()
                    info.oppo_attack = cons
                elif self.skill > info.player.skill and self.speed > info.player.speed:
                    info.oppo_attack = norm
                else:
                    info.oppo_attack = norm
            print(f"\n{self.name} is fighting {info.oppo_attack}.")
        elif self.pl_controlled == True:
            f = input(f"\nWould {info.player.name} like to attack:\nconservatively (type 'c')\naggressively (type 'a')\nnormal (press enter)\n\n> ")
            if f.lower() == "c":
                self.fight_conservative()
                info.pl_attack = cons
            elif f.lower() == "a":
                self.fight_aggressive()
                info.pl_attack = aggr
            else:
                info.pl_attack = norm
            print(f"\n{self.name} is fighting {info.pl_attack}.")


#: without setting player.name to pl_name here, player.name doesn't update.
def get_player_name():
    info.pl_name = input("\nWhat is the name of your character?\n> ")
    info.player.name = info.pl_name
