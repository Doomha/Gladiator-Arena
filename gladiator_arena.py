import random
from sys import exit

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

weapon_ls = [Sword(), Bow(), Spear(), Rock()]
contestants_ls = [Contestant("James", 4, 8, 7), Contestant("Jack", 6, 6, 6), Contestant("Jaxon", 8, 7, 5)]
attack_evade_mod = 0.1
hit_chance = 10
start_health = 10
turnCount = 0

def explain(info):
    print(info)
    input("Please press 'enter' to continue.")

def fight_explain():
    explain("\tWelcome to the fighting pits! Your goal is to reduce your opponents' health to 0. Contestants, including yourself, start with 10 health points, so don't worry if your opponent hits you every so often. This is a game of survival, not (necessarily) who hits first!")
    explain("\n\tThere are a couple of other stats that will be important to remember...")
    explain("\n\nSkill: The chance one of your attacks hits your opponent.")
    explain("\nSpeed: Decides who gets to attack first.")
    explain("\nStrength: How hard one of your attacks hits, once it connects with your opponent.")
    explain("\n\n\tThat being said, your equipment has an impact on your stats as well. Choose a cumbersome weapon, and your Speed will go down. Attack with something small, and your Strength doesn't do much good.\n\n\t\t\t\t\tGood luck!\n\n")
    explain("\n\n\n\n\n")

def weapon_pick():
    print("Here are the weapons you can choose from:")
    for weapon in weapon_ls:
        print(weapon.name)
    print(f"Out of these {len(weapon_ls)} options, you can only pick one.")
    for weapon in weapon_ls:
        weapon_select = input(f"Would you like to use a {weapon.name}?\n> ")
        if weapon_select.lower() == 'yes':
            player.weapon = weapon
            print(f"You've chosen to fight with a {weapon.name}.")
            break

def arena_enter():
    explain("\nYou're ready to fight! There are several other contestants.")
    for count,contestant in enumerate(contestants_ls,1):
        print(f"Contestant {count} is: " + contestant.name)

    opponent = contestants_ls[int(input("Please type the number of the contestant you would like to duel.\n> ")) - 1]
    opponent.weapon = random.choice(weapon_ls)
    explain(f"\n{opponent.name} will be fighting you with a {opponent.weapon.name}. Good luck!\n")

def combat_stats():
    print(f"{opponent.name}'s skill: {opponent.skill}, speed: {opponent.speed}, strength: {opponent.strength}.\n")
    explain(f"{player.name}'s skill: {player.skill}, speed: {player.speed}, strength: {player.strength}.\n")
    print("\nHere's how the weapons of you and your opponent impacted your stats...\n")
    print(opponent.weapon.w_type)
    print(f"{opponent.name}'s skill: {opponent.skill}, speed: {opponent.getSpeed()}, potential damage: {opponent.getDamage()}.\n")
    explain(f"{player.name}'s skill: {player.skill}, speed: {player.getSpeed()}, potential damage: {player.getDamage()}.\n")


def attack_init():
    global turnCount
    if player.getSpeed() > opponent.getSpeed():
        explain("\nYou are faster than your opponent. You attack first.\n")
    elif player.getSpeed() < opponent.getSpeed():
        explain("\nYour opponent is faster than you. They attack first.\n")
        turnCount += 1
    else:
        chance = random.randrange(0, 2)
        if chance == 0:
            explain("\nNeither you nor your opponent is faster, but your opponent gains the upper hand.\n")
            turnCount += 1
        else:
            explain("\nNeither you nor your opponent is faster, but you gain the upper hand.\n")
    attack()


def attack():
    global turnCount
    chance = random.randrange(0, hit_chance)
    if turnCount % 2 == 0:
        b = "Your"
        source = player
        target = opponent
    else:
        b = "Their"
        source = opponent
        target = player
    if source.skill + chance >= hit_chance:
        explain(f"{b} attack hits!\n")
        damage_done = round(source.getDamage() - ((target.skill + target.speed) * attack_evade_mod))

        if damage_done >= 0:
            print(f"You did {damage_done} damage.")
            target.takeDamage(damage_done)
        else:
            print(f"You did 1 damage.")
            target.takeDamage(1)
        explain(f"{target.name} has {target.health} left.\n")
    else:
        explain(f"{b} attack misses.\n")
    win_condition()
    turnCount += 1
    attack()

def win_condition():
    if opponent.health <= 0:
        explain("\n\n\n\t\t\t\t\tYou win!\n\n\n\n\n")
        quit()
    elif player.health <= 0:
        explain("\n\n\n\t\t\t\t\tYou lose.\n\n\n\n\n")
        quit()


pl_name = input("What is your name?\n> ")
player = Contestant(pl_name, 5, 5, 5)
opponent = contestants_ls[0]
check_explain = input("Would you like an explanation of how this works?\n> ")
if check_explain.lower() == "yes":
    fight_explain()
weapon_pick()
arena_enter()
combat_stats()
attack_init()
