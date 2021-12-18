import random
from sys import exit
import glad_classes as classes
import glad_items as items
import glad_inventory as inventory
import glad_opponents as oppo

weapon_ls = [items.Sword(), items.Bow(), items.Spear(), items.Warhammer(), items.Fist()]
armor_ls = [items.Chainmail(), items.Platemail(), items.StuddedLeather(), items.Tunic()]
contestants_ls = [classes.Contestant("James", False, None, None, None), classes.Contestant("Jack", False, None, None, None), classes.Contestant("Jaxon", False, None, None, None), classes.Contestant("Jordan", False, None, None, None), classes.Contestant("Jerry", False, None, None, None), classes.Contestant("Jay", False, None, None, None), classes.Contestant("Joel", False, None, None, None), classes.Contestant("Jasper", False, None, None, None)]
game_mode_ls = [oppo.EasyMode(), oppo.NormalMode(), oppo.HardMode()]
game_mode = None
attack_evade_mod = 0.1
hit_chance = 10
turnCount = 0
valid_opponent_input = 0
opponent = contestants_ls[0]
pl_name = None
health_reset = None
strength_reset = None
defense_reset = None
speed_reset = None
item_find = None
seller = None
buyer = None
transaction_verb = None
player = classes.Contestant(pl_name, True, None, None, None)
shopkeeper = inventory.Person("Ginger", False, 15, 3, 4, 5, 6)
