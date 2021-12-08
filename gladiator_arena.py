import random
from sys import exit

class Weapon:
    def __init__(self, w_name, w_type, w_speed, w_damage):
        self.w_name = w_name
        self.w_type = w_type
        self.w_speed = w_speed
        self.w_damage = w_damage

class Ranged_weapon(Weapon):
    def __init__(self, w_name, w_type, w_speed, w_damage, w_range):
        super().__init__(w_name, w_type, w_speed, w_damage)
        self.w_range = w_range

class Melee_weapon(Weapon):
    def __init__(self, w_name, w_type, w_speed, w_damage, w_power):
        super().__init__(w_name, w_type, w_speed, w_damage)
        self.w_power = w_power

class Magic_weapon(Weapon):
    def __init__(self, w_name, w_speed, w_damage, w_sp_power):
        super().__init__(w_name, w_speed, w_damage)
        self.w_sp_power = w_sp_power

class Armor:
    def __init__(self, a_name, a_defense, a_weight):
        self.a_name = a_name
        self.a_defense = a_defense
        self.a_weight = a_weight

class Magic_armor(Armor):
    def __init__(self, a_name, a_defense, a_weight, a_magic_buff):
        super().__init__(a_name, a_defense, a_weight)
        self.a_magic_buff = a_magic_buff

class Contestant:
    def __init__(self, c_name, c_skill, c_speed, c_strength):
        self.c_name = c_name
        self.c_skill = c_skill
        self.c_speed = c_speed
        self.c_strength = c_strength

class Stats:
    def __init__(self, skill, speed, damage, health):
        self.skill = skill
        self.speed = speed
        self.damage = damage
        self.health = health

pl_weapons = []
opp_weapons = []
sword = Melee_weapon("Sword", "melee", 4, 7, 5)
bow = Ranged_weapon("Bow", "ranged", 5, 5, 8)
spear = Melee_weapon("Spear", "melee", 6, 4, 3)
rock = Melee_weapon("Rock", "melee", 1, 1, 1)
weapon_ls = [sword, bow, spear, rock]
contest1 = Contestant("James", 4, 8, 7)
contest2 = Contestant("Jack", 6, 6, 6)
contest3 = Contestant("Jaxon", 8, 7, 5)
contestants_ls = [contest1, contest2, contest3]
picked_opp = []
calc = float(2)
priority = 2
attack_evade_mod = 0.1
hit_chance = 10
start_health = 10

def intro():
    global pl_name
    global player
    pl_name = input("What is your name?\n> ")
    player = Contestant(pl_name, 5, 5, 5)
    explain = input("Would you like an explanation of how this works?\n> ")
    if explain == "Yes" or explain == "yes":
        fight_explain()
    else:
        weapon_pick()

def fight_explain():
    print("\tWelcome to the fighting pits! Your goal is to reduce your opponents' health to 0. Contestants, including yourself, start with 10 health points, so don't worry if your opponent hits you every so often. This is a game of survival, not (necessarily) who hits first!")
    input("Please press 'enter' to continue.")
    print("\n\tThere are a couple of other stats that will be important to remember...")
    input("Please press 'enter' to continue.")
    print("\n\nSkill: The chance one of your attacks hits your opponent.")
    input("Please press 'enter' to continue.")
    print("\nSpeed: Decides who gets to attack first.")
    input("Please press 'enter' to continue.")
    print("\nStrength: How hard one of your attacks hits, once it connects with your opponent.")
    input("Please press 'enter' to continue.")
    print("\n\n\tThat being said, your equipment has an impact on your stats as well. Choose a cumbersome weapon, and your Speed will go down. Attack with something small, and your Strength doesn't do much good.")
    print("\n\n\t\t\t\t\tGood luck!\n\n")
    input("Please press 'enter' to continue.\n\n\n\n\n")
    weapon_pick()

def weapon_pick():
    weapon_num = len(weapon_ls)
    print("Here are the weapons you can choose from:")
    count = 0
    for i in weapon_ls:
        print(weapon_ls[count].w_name)
        count += 1
    print(f"Out of these {weapon_num} options, you can only pick one.")
    count = 0
    for k in weapon_ls:
        weapon_select = input(f"Would you like to use a {weapon_ls[count].w_name}?\n> ")
        if "yes" in weapon_select or "Yes" in weapon_select:
            picked_weapon = weapon_ls[count]
            pl_weapons.append(picked_weapon)
            print(f"You've chosen to fight with a {picked_weapon.w_name}.")
            break
        else:
            count += 1
    arena_enter()

def arena_enter():
    print("\nYou're ready to fight! There are several other contestants.")
    input("Please press 'enter' to continue.")

    count = 1
    for y in contestants_ls:
        shown_opp = y
        print(f"Contestant {count} is: " + shown_opp.c_name)
        count += 1

    opp_pick = contestants_ls[int(input("Please type the number of the contestant you would like to duel.\n> ")) - 1]
    opp_w_pick = random.choice(weapon_ls)
    opp_weapons.append(opp_w_pick)
    picked_opp.append(opp_pick)
    print(f"\n{opp_pick.c_name} will be fighting you with a {opp_w_pick.w_name}. Good luck!\n")
    input("Please press 'enter' to continue.\n\n\n\n\n")
    combat_stats()

def combat_stats():
    print(f"{picked_opp[0].c_name}'s skill: {picked_opp[0].c_skill}, speed: {picked_opp[0].c_speed}, strength: {picked_opp[0].c_strength}.\n")
    print(f"{player.c_name}'s skill: {player.c_skill}, speed: {player.c_speed}, strength: {player.c_strength}.\n")
    input("Please press 'enter' to continue.")
    print("\nHere's how the weapons of you and your opponent impacted your stats...\n")
    stats_creator()
    print(f"{picked_opp[0].c_name}'s skill: {opp_stats.skill}, speed: {opp_stats.speed}, potential damage: {opp_stats.damage}.\n")
    print(f"{player.c_name}'s skill: {pl_stats.skill}, speed: {pl_stats.speed}, potential damage: {pl_stats.damage}.\n")
    input("Please press 'enter' to continue.")
    attack_priority()

def stats_creator():
    global opp_stats
    global pl_stats

    if opp_weapons[0].w_type == "melee":
        print("melee")
    elif opp_weapons[0].w_type == "ranged":
        print("ranged")
    elif opp_weapons[0].w_type == "magic":
        print("magic")
    else:
        print("nothing")

    opp_skill = float(picked_opp[0].c_skill)
    opp_speed = float((picked_opp[0].c_speed + opp_weapons[0].w_speed) / 2)
    opp_damage = float((picked_opp[0].c_strength + opp_weapons[0].w_damage) / 2)
    opp_health = start_health
    opp_stats = Stats(opp_skill, opp_speed, opp_damage, opp_health)

    pl_skill = float(player.c_skill)
    pl_speed = float((player.c_speed + pl_weapons[0].w_speed) / 2)
    pl_damage = float((player.c_strength + pl_weapons[0].w_damage) / 2)
    pl_health = start_health
    pl_stats = Stats(pl_skill, pl_speed, pl_damage, pl_health)

def attack_priority():
    if pl_stats.speed > opp_stats.speed:
        priority = 1
        print("\nYou are faster than your opponent. You attack first.\n")
        input("Please press 'enter' to continue.")
    elif pl_stats.speed < opp_stats.speed:
        priority = 0
        print("\nYour opponent is faster than you. They attack first.\n")
        input("Please press 'enter' to continue.")
    else:
        chance = random.randrange(0, 2)
        if chance == 0:
            priority = 0
            print("\nNeither you nor your opponent is faster, but your opponent gains the upper hand.\n")
            input("Please press 'enter' to continue.")
        else:
            priority = 1
            print("\nNeither you nor your opponent is faster, but you gain the upper hand.\n")
            input("Please press 'enter' to continue.")
    whos_attacking()

def whos_attacking():
    if priority == 1:
        calc = pl_stats.skill
        attack_check()
    else:
        calc = opp_stats.skill
        attack_check()

def attack_check():
    global priority
    if priority == 1:
        b = "Your"
    else:
        b = "Their"
    chance = random.randrange(0, hit_chance)
    if calc + chance >= hit_chance:
        print(f"{b} attack hits!\n")
        input("Please press 'enter' to continue.")
        hit = True
        damage_calc()
    else:
        print(f"{b} attack misses.\n")
        input("Please press 'enter' to continue.")
        hit = False
        if priority == 1:
            priority = 0
            whos_attacking()
        else:
            priority = 1
            whos_attacking()

def damage_calc():
    if priority == 1:
        damage_done = round(pl_stats.damage - ((opp_stats.skill + opp_stats.speed) * attack_evade_mod))
        if damage_done >= 0:
            opp_stats.health = opp_stats.health - damage_done
            print(f"You did {damage_done} damage.")
        else:
            opp_stats.health = opp_stats.health - 1
            print(f"You did 1 damage.")
        print(f"{picked_opp[0].c_name} has {opp_stats.health} left.\n")
        input("Please press 'enter' to continue.")
    else:
        damage_done = round(opp_stats.damage - ((opp_stats.skill + opp_stats.speed) * attack_evade_mod))
        if damage_done >= 0:
            pl_stats.health = pl_stats.health - damage_done
            print(f"{picked_opp[0].c_name} did {damage_done} damage.")
        else:
            pl_stats.health = pl_stats.health - 1
            print(f"{picked_opp[0].c_name} did 1 damage to you.")
        print(f"You have {pl_stats.health} left.\n")
        input("Please press 'enter' to continue.")
    win_condition()

def win_condition():
    global priority
    if opp_stats.health <= 0:
        print("\n\n\n\t\t\t\t\tYou win!\n\n\n\n\n")
        input("Please press 'enter' to continue.")
        quit()
    elif pl_stats.health <= 0:
        print("\n\n\n\t\t\t\t\tYou lose.\n\n\n\n\n")
        input("Please press 'enter' to continue.")
        quit()
    elif priority == 1:
        priority = 0
    else:
        priority = 1
    whos_attacking()

intro()
