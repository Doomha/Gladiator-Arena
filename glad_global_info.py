import random
from sys import exit
import glad_classes as classes

weapon_ls = [classes.Sword(), classes.Bow(), classes.Spear(), classes.Rock()]
contestants_ls = [classes.Contestant("James", 4, 8, 7), classes.Contestant("Jack", 6, 6, 6), classes.Contestant("Jaxon", 8, 7, 5)]
attack_evade_mod = 0.1
hit_chance = 10
turnCount = 0
