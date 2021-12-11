import random
from sys import exit
import glad_classes as classes
import glad_items as items

weapon_ls = [items.Sword(), items.Bow(), items.Spear(), items.Rock()]
armor_ls = [items.Chainmail(), items.Platemail(), items.Tunic()]
contestants_ls = [classes.Contestant("James", False, 4, 8, 7, 0, 0, 0), classes.Contestant("Jack", False, 6, 6, 6, 0, 0, 0), classes.Contestant("Jaxon", False, 8, 7, 5, 0, 0, 0)]
attack_evade_mod = 0.1
hit_chance = 10
turnCount = 0
valid_opponent_input = 0
opponent = None
pl_name = None
start_health = None #: This gets used to reset player health for new fight
player = classes.Contestant(pl_name, True, 6, 6, 6, 10, 4, 3)
