import random
from sys import exit
import glad_global_info as info
import glad_classes as classes
import glad_items as items
import glad_inventory as inventory
global opponent

def explain(info):
    print(info)
    input("Please press 'enter' to continue.")

def lines_start(content):
    print(content)
    print("-" * 10)

def lines_end(content):
    print(content + ("-" * 10))

def explanation():
    check_explain = input("Would you like an explanation of how this works?\n> ")
    if check_explain.lower() == "yes":
        fight_explain()

def fight_explain():
    explain("\tWelcome to the fighting pits! Your goal is to reduce your opponents' health to 0. Contestants, including yourself, start with 10 health points, so don't worry if your opponent hits you every so often. This is a game of survival, not (necessarily) who hits first!")
    explain("\n\tThere are a couple of other stats that will be important to remember...")
    explain("\n\nSkill: The chance one of your attacks hits your opponent. Also helps you dodge your opponent's attacks.")
    explain("\nSpeed: Decides who gets to attack first. Also helps you dodge your opponent's attacks.")
    explain("\nStrength: How hard one of your attacks hits, once it connects with your opponent.")
    explain("\n\n\tThat being said, your equipment has an impact on your stats as well. Choose a cumbersome weapon, and your Speed will go down. Attack with something small, and your Strength doesn't do much good.\n\n\t\t\t\t\tGood luck!\n\n")
    explain("\n\n\n\n\n")

def weapon_pick():
    lines_start("\nHere are the weapons you can choose from:")
    for weapon in info.weapon_ls:
        print(f"{weapon.name} -- value: {weapon.value} speed: {weapon.speed} damage: {weapon.damage}")
    lines_end("")
    print(f"\nOut of these {len(info.weapon_ls)} options, you can only pick one.\n")
    for weapon in info.weapon_ls:
        weapon_select = input(f"Would you like to use a {weapon.name}?\n> ")
        if weapon_select.lower() == 'yes':
            info.player.weapon = weapon
            lines_start(f"\nYou've chosen to fight with a {weapon.name}.")
            break

def armor_pick():
    lines_start("\nHere are the armor options you can choose from:")
    for armor in info.armor_ls:
        print(f"{armor.name} -- value: {armor.value} defense: {armor.defense} weight: {armor.weight}")
    lines_end("")
    print(f"\nOut of these {len(info.armor_ls)} options, you can only pick one.\n")
    for armor in info.armor_ls:
        armor_select = input(f"Would you like to use {armor.name}?\n> ")
        if armor_select.lower() == 'yes':
            info.player.armor = armor
            lines_start(f"\nYou've chosen to fight with {armor.name}.")
            break

def arena_enter():
    explain("\nYou're ready to fight! There are several other contestants.")
    lines_end("\n")
    for count,contestant in enumerate(info.contestants_ls,1):
        print(f"Contestant {count} is: {contestant.name}. Their stats are: {contestant.skill} skill, {contestant.speed} speed, {contestant.strength} strength.")
    lines_end("")
    def opponent_input_check():
        opponent_input = input("\nPlease type the number of the contestant you would like to duel.\n> ")
        if opponent_input.isnumeric() != True or int(opponent_input) > count or int(opponent_input) <= 0:
            print("It looks like you haven't typed in a valid number. Please try again.\n")
            opponent_input_check()
        else:
            info.valid_opponent_input = int(opponent_input)

    opponent_input_check()
    info.opponent = info.contestants_ls[info.valid_opponent_input - 1]
    info.opponent.weapon = random.choice(info.weapon_ls)
    info.opponent.armor = random.choice(info.armor_ls)
    explain(f"\n{info.opponent.name} will be fighting you with a {info.opponent.weapon.name}, which is a {info.opponent.weapon.w_type} weapon. They are also equipped with {info.opponent.armor.name}. Good luck!\n")

def combat_stats():
    lines_end("\n")
    print(f"\n{info.opponent.name}'s skill: {info.opponent.skill}, speed: {info.opponent.speed}, strength: {info.opponent.strength}.\n")
    explain(f"{info.player.name}'s skill: {info.player.skill}, speed: {info.player.speed}, strength: {info.player.strength}.\n")
    print("\nHere's how the weapons and armor of you and your opponent impacted your stats...\n")
    info.opponent.getDefense()
    info.player.getDefense()
    print(f"\n{info.opponent.name}'s skill: {round(info.opponent.skill)}, speed: {round(info.opponent.getSpeed())}, damage: {round(info.opponent.getDamage())}, defense: {round(info.opponent.defense)}.\n")
    explain(f"{info.player.name}'s skill: {round(info.player.skill)}, speed: {round(info.player.getSpeed())}, damage: {round(info.player.getDamage())}, defense: {round(info.player.defense)}.\n")


def attack_init():
    if info.player.getSpeed() > info.opponent.getSpeed():
        explain("\n\nYou are faster than your opponent. You attack first.\n")
    elif info.player.getSpeed() < info.opponent.getSpeed():
        explain("\n\nYour opponent is faster than you. They attack first.\n")
        info.turnCount += 1
    else:
        chance = random.randrange(0, 2)
        if chance == 0:
            explain("\n\nNeither you nor your opponent is faster, but your opponent gains the upper hand.\n")
            info.turnCount += 1
        else:
            explain("\n\nNeither you nor your opponent is faster, but you gain the upper hand.\n")
    attack()


def attack():
    chance = random.randrange(0, info.hit_chance)
    if info.turnCount % 2 == 0:
        b = info.player.name
        source = info.player
        target = info.opponent
    else:
        b = info.opponent.name
        source = info.opponent
        target = info.player
    if source.skill + chance >= info.hit_chance:
        explain(f"\n{b}'s attack hits!\n")
        damage_done = round(source.getDamage() - (((target.skill + target.speed) * info.attack_evade_mod) + target.defense))

        if damage_done >= 0:
            print(f"{b} damage done was {damage_done}. {target.name}'s {target.armor.name} blocked {round(target.defense)} damage.")
            target.takeDamage(damage_done)
        else:
            print(f"1 damage was done.")
            target.takeDamage(1)
        print(f"{target.name} has {target.health} health left.\n")
        win_condition()
        if prompt_inventory() == True:
            if use_inventory() == True:
                trigger_item_effect()

    else:
        explain(f"{b} attack misses.\n")
    info.turnCount += 1
    attack()

def prompt_inventory():
    a = input("Would you like to view your inventory?\n> ")
    if a.lower() != "yes":
        return
    elif a.lower() == "yes" or a.lower() == "y":
        info.player.ls_inventory()
        b = input("Would you like to use an item?\n> ")
        if b.lower() != "yes":
            return False
        elif b.lower() == "yes" or b.lower() == "y":
            return True

def use_inventory():
    if info.player.item_exist() == False:
        return explain("")
    if info.player.item_consume_check() == False:
        return explain("")
    if info.player.item_inventory_check() == False:
        return explain("")
    info.player.consume_item()
    return True

def trigger_item_effect():
    if info.player.health_increase_check() > 0:
        health_incr = info.player.health_increase_check()
        info.player.increaseHealth(health_incr)
        explain(f"{info.player.name}'s health increased by {health_incr}, and is now {info.player.health}.\n")

    elif info.player.strength_increase_check() > 0:
        strength_incr = info.player.strength_increase_check()
        info.player.increaseStrength(strength_incr)
        explain(f"{info.player.name}'s strength increased by {strength_incr}, and is now {info.player.strength}.\n")

    elif info.player.defense_increase_check() > 0:
        defense_incr = info.player.defense_increase_check()
        info.player.increaseDefense(defense_incr)
        explain(f"{info.player.name}'s defense increased by {defense_incr}, and is now {info.player.armor.defense}.\n")

    elif info.player.speed_increase_check() > 0:
        speed_incr = info.player.speed_increase_check()
        info.player.increaseSpeed(speed_incr)
        explain(f"{info.player.name}'s speed increased by {speed_incr}, and is now {info.player.speed}.\n")
    else:
        pass

def win_condition():
    if info.opponent.health <= 0 and (len(info.contestants_ls) - 1) > 0:
        c = info.contestants_ls.index(info.opponent)
        info.contestants_ls.pop(c)
        explain(f"\nYou beat {info.opponent.name}!\n")
        lines_start("")
        play_again()
    elif info.opponent.health <= 0 and (len(info.contestants_ls) - 1) == 0:
        print(f"\n\n\t\t\t\t\tYou beat {info.opponent.name}!")
        lines_end("\n\n\t\t\t\t\tYou win!\n\n\n\n\n")
        quit()
    elif info.player.health <= 0:
        print("\n\n\n\t\t\t\t\tYou lose.\n\n\n\n\n")
        r = input("Would you like to play again?\n> ")
        if r.lower() == "yes" or r.lower() == "y":
            info.player.health = info.start_health
            info.opponent.health = info.start_health
            lines_start("")
            classes.get_player_name()
            weapon_pick()
            armor_pick()
            arena_enter()
            combat_stats()
            attack_init()
        else:
            quit()

def play_again():
    r = input("\nWould you like to play again? Your combat stats will reset, but your health will remain the same.\n> ")
    if r.lower() == "yes" or r.lower() == "y":
        info.player.strength = info.strength_reset
        info.player.defense = info.defense_reset
        info.player.speed = info.speed_reset
        arena_enter()
        combat_stats()
        attack_init()
    else:
        q = input("Are you sure? Type 'q' to quit.\n> ")
        if q.lower() == "q":
            quit()
        else:
            play_again()




explanation()
classes.get_player_name()
weapon_pick()
armor_pick()
arena_enter()
combat_stats()
attack_init()
