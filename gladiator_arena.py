import random
from sys import exit
import glad_global_info as info
import glad_classes as classes
import glad_items as items
import glad_inventory as inventory
import glad_opponents as oppo
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

def show_difficulty():
    diff_input = input("Would you like to choose the level of difficulty?\n> ")
    if diff_input.lower() != "yes":
        info.game_mode = info.game_mode_ls[1]
    elif diff_input.lower() == "yes":
        print("Here are the levels of difficulty:\n")
        count = 0
        for a in enumerate(info.game_mode_ls):
            print(info.game_mode_ls[count])
            count += 1
        choose_difficulty()
    explain(f"\nYou're playing on {info.game_mode} mode.")

def choose_difficulty():
    chosen_diff = input(f"\nType in the level of difficulty you would like to play.\n> ")
    count = 0
    for b in enumerate(info.game_mode_ls):
        if chosen_diff.lower() == info.game_mode_ls[count].lower():
            info.game_mode = info.game_mode_ls[count]
        elif count == len(info.game_mode_ls):
            explain("It looks like you haven't typed in a valid game mode. Try again.")
            choose_difficulty()
        else:
            count += 1

def fight_explain():
    explain("\tWelcome to the fighting pits! Your goal is to reduce your opponents' health to 0. Contestants, including yourself, start with 10 health points, so don't worry if your opponent hits you every so often. This is a game of survival, not (necessarily) who hits first!")
    explain("\n\tThere are a couple of other stats that will be important to remember...")
    explain("\n\nSkill: The chance one of your attacks hits your opponent. Also helps you dodge your opponent's attacks.")
    explain("\nSpeed: Decides who gets to attack first. Also helps you dodge your opponent's attacks.")
    explain("\nStrength: How hard one of your attacks hits, once it connects with your opponent.")
    explain("\n\n\tThat being said, your equipment has an impact on your stats as well. Choose a cumbersome weapon, and your Speed will go down. Attack with something small, and your Strength doesn't do much good.\n\n\t\t\t\t\tGood luck!\n\n")
    explain("\n\n\n\n\n")

def weapon_pick():
    lines_start(f"\nHere are the weapons {info.player.name} can choose from:")
    for weapon in info.weapon_ls:
        print(f"{weapon.name} -- speed: {weapon.speed} damage: {weapon.damage} value: {weapon.value}")
    lines_end("")
    print(f"\nOut of these {len(info.weapon_ls)} options, {info.player.name} can only pick one.\n")
    for weapon in info.weapon_ls:
        weapon_select = input(f"Would {info.player.name} like to use a {weapon.name}?\n> ")
        if weapon_select.lower() == 'yes' or weapon_select.lower() == 'y':
            info.player.weapon = weapon
            lines_start(f"\n{info.player.name} has chosen to fight with a {weapon.name}.")
            break

def armor_pick():
    lines_start(f"\nHere are the armor options {info.player.name} can choose from:")
    for armor in info.armor_ls:
        print(f"{armor.name} -- value: {armor.value} defense: {armor.defense} weight: {armor.weight}")
    lines_end("")
    print(f"\nOut of these {len(info.armor_ls)} options, {info.player.name} can only pick one.\n")
    for armor in info.armor_ls:
        armor_select = input(f"Would {info.player.name} like to use {armor.name}?\n> ")
        if armor_select.lower() == 'yes' or armor_select.lower() == 'y':
            info.player.armor = armor
            lines_start(f"\n{info.player.name} has chosen to fight with {armor.name}.")
            break

def visit_shop():
    print(f"Before entering the arena, {info.player.name} passes by a shop called {info.shopkeeper.name}'s Gladiator Goods.\n")
    a = input(f"Would {info.player.name} like to enter the shop?\n> ")
    if a.lower() != "yes":
        return
    else:
        shop_loop()

def shop_loop():
    if shop_inside() != False:
        if valid_item_shop() != False:
            if seller_item_check() != False:
                buy_from_seller()

def shop_inside():
    info.shopkeeper.ls_inventory_prices()
    info.player.ls_inventory()
    b = input(f"Would {info.player.name} like to buy, sell, or leave?\n> ")
    if b.lower() == "buy" or b.lower() == "b":
        info.seller = info.shopkeeper
        info.buyer = info.player
        info.transaction_verb = "buy"
    elif b.lower() == "sell" or b.lower() == "s":
        info.seller = info.player
        info.buyer = info.shopkeeper
        info.transaction_verb = "sell"
    else:
        return False

def valid_item_shop():
    #: Is the selected item valid?
    info.item_find = len(info.seller.pouch) - 1
    p = input(f"What would {info.player.name} like to {info.transaction_verb}?\n> ")
    item_picked = p.lower()
    for n in info.seller.pouch:
        if info.seller.pouch[info.item_find].name == item_picked:
            break
        elif info.seller.pouch[info.item_find].name[0: -1] == item_picked:
            break
        elif info.seller.gold.name == item_picked:
            print(f"{info.player.name} can't {info.transaction_verb} {info.seller.gold.name}!")
            continue_shopping()
            return False
        elif info.item_find == 0:
            print(f"It looks like {info.seller.name} doesn't have that item right now.")
            continue_shopping()
            return False
        info.item_find -= 1

def seller_item_check():
    #: Does seller have the item?
    if info.seller.pouch[info.item_find].amount == 0:
        explain(f"{info.seller.name} doesn't have enough {info.seller.pouch[info.item_find].name} right now.")
        continue_shopping()
        return False
    elif info.buyer.gold.amount < info.seller.pouch[info.item_find].value:
        explain(f"{info.buyer.name} doesn't have enough gold right now.")
        continue_shopping()
        return False

def buy_from_seller():
    info.buyer.gold.amount -= info.seller.pouch[info.item_find].value
    info.buyer.pouch[info.item_find].amount += 1
    info.seller.pouch[info.item_find].amount -= 1
    explain(f"{info.buyer.name} bought 1 {info.buyer.pouch[info.item_find].name} from {info.seller.name}.\n")
    continue_shopping()
    return

def continue_shopping():
    c = input(f"Would {info.player.name} like to continue shopping?\n> ")
    if c.lower() == "yes":
        shop_loop()
    else:
        return False

def arena_enter():
    explain(f"\n{info.player.name} enters the arena to thunderous applause.\n\nAs {info.player.name} looks around, {info.player.name} notices that there are several other contestants.")
    lines_end("\n")
    for count,contestant in enumerate(info.contestants_ls,1):
        print(f"Contestant {count} is: {contestant.name}. Their stats are: {contestant.skill} skill, {contestant.speed} speed, {contestant.strength} strength.")
    lines_end("")
    def opponent_input_check():
        opponent_input = input(f"\nWhich contestant should {info.player.name} duel?\n> ")
        if opponent_input.isnumeric() != True or int(opponent_input) > count or int(opponent_input) <= 0:
            print("It looks like you haven't typed in a valid number. Please try again.\n")
            opponent_input_check()
        else:
            info.valid_opponent_input = int(opponent_input)

    opponent_input_check()
    info.opponent = info.contestants_ls[info.valid_opponent_input - 1]
    oppo.get_weapon()
    info.opponent.armor = random.choice(info.armor_ls)
    explain(f"\n{info.opponent.name} will be fighting you with a {info.opponent.weapon.name}, which is a {info.opponent.weapon.w_type} weapon. They are also equipped with {info.opponent.armor.name}. Good luck!\n")

def combat_stats():
    lines_end("\n")
    print(f"\n{info.opponent.name}'s skill: {info.opponent.skill}, speed: {info.opponent.speed}, strength: {info.opponent.strength}.\n")
    explain(f"{info.player.name}'s skill: {info.player.skill}, speed: {info.player.speed}, strength: {info.player.strength}.\n")
    print(f"\nHere's how the weapons and armor of {info.player.name} and {info.opponent.name} impacted their stats...\n")
    info.opponent.getDefense()
    info.player.getDefense()
    print(f"\n{info.opponent.name}'s skill: {round(info.opponent.skill)}, speed: {round(info.opponent.getSpeed())}, damage: {round(info.opponent.getDamage())}, defense: {round(info.opponent.defense)}.\n")
    explain(f"{info.player.name}'s skill: {round(info.player.skill)}, speed: {round(info.player.getSpeed())}, damage: {round(info.player.getDamage())}, defense: {round(info.player.defense)}.\n")


def attack_init():
    def attack_priority(scenario):
        if scenario == True:
            explain(f"\n{faster} is faster than {slower}, so {faster} attacks first.\n")
        else:
            print(f"\n\nNeither {info.player.name} or {info.opponent.name} is faster.")

    if round(info.player.getSpeed()) == round(info.opponent.getSpeed()):
        chance = random.randrange(0, 2)
        if chance == 0:
            attack_priority(False)
            explain(f"However, {info.opponent.name} gains the upper hand and attacks.")
            info.turnCount += 1
        else:
            attack_priority(False)
            explain(f"However, {info.player.name} gains the upper hand and attacks.")
    else:
        if info.player.getSpeed() > info.opponent.getSpeed():
            faster = info.player.name
            slower = info.opponent.name
        elif info.player.getSpeed() < info.opponent.getSpeed():
            faster = info.opponent.name
            slower = info.player.name
            info.turnCount += 1
        attack_priority(True)
    attack()


def attack():
    chance = random.randrange(0, info.hit_chance)
    if info.turnCount % 2 == 0:
        source = info.player
        target = info.opponent
    else:
        source = info.opponent
        target = info.player
    if source.skill + chance >= info.hit_chance:
        explain(f"\n{source.name}'s attack hits!\n")
        damage_done = round(source.getDamage() - (((target.skill + target.speed) * info.attack_evade_mod) + target.defense))

        if damage_done >= 0:
            print(f"{source.name} did {damage_done} damage. {target.name}'s {target.armor.name} blocked {round(target.defense)} damage.")
            target.takeDamage(damage_done)
        else:
            print(f"1 damage was done.")
            target.takeDamage(1)
        print(f"{target.name} has {target.health} health left.\n")
        win_condition()
        inventory_loop()
    else:
        explain(f"{source.name} attack misses.\n")
    info.turnCount += 1
    attack()

def inventory_loop():
    if prompt_inventory() == True:
        if use_inventory() == True:
            info.player.consume_item()
            trigger_item_effect()

def prompt_inventory():
    a = input(f"Would {info.player.name} like to view their inventory?\n> ")
    if a.lower() != "yes":
        print("")
        return
    else:
        info.player.ls_inventory()
        b = input(f"Would {info.player.name} like to use an item?\n> ")
        if b.lower() != "yes":
            print("")
            return False
        else:
            return True

def use_inventory():
    if info.player.item_exist() == False:
        return explain("")
    if info.player.item_consume_check() == False:
        return explain("")
    if info.player.item_inventory_check() == False:
        return explain("")
    return True

def trigger_item_effect():
    def item_explanation(stat_name, increase, stat):
        explain(f"{info.player.name}'s {stat_name} increased by {increase}, and is now {stat}.\n")

    if info.player.health_increase_check() > 0:
        health_incr = info.player.health_increase_check()
        info.player.increaseHealth(health_incr)
        stat = round(info.player.health)
        item_explanation("health", health_incr, stat)

    elif info.player.strength_increase_check() > 0:
        strength_incr = info.player.strength_increase_check()
        info.player.increaseStrength(strength_incr)
        stat = round(info.player.strength)
        item_explanation("strength", strength_incr, stat)

    elif info.player.defense_increase_check() > 0:
        defense_incr = info.player.defense_increase_check()
        info.player.increaseDefense(defense_incr)
        stat = round(info.player.defense)
        item_explanation("defense", defense_incr, stat)

    elif info.player.speed_increase_check() > 0:
        speed_incr = info.player.speed_increase_check()
        info.player.increaseSpeed(speed_incr)
        stat = round(info.player.speed)
        item_explanation("speed", speed_incr, stat)

def win_condition():
    if info.opponent.health <= 0 and (len(info.contestants_ls) - 1) > 0:
        c = info.contestants_ls.index(info.opponent)
        info.contestants_ls.pop(c)
        explain(f"\n{info.player.name} beat {info.opponent.name}!\n")
        info.opponent.ls_inventory()
        opponent_drop()
        play_again()
    elif info.opponent.health <= 0 and (len(info.contestants_ls) - 1) == 0:
        print(f"\n\n\t\t\t\t\t{info.player.name} beat {info.opponent.name}!")
        lines_end(f"\n\n\t\t\t\t\t{info.player.name} wins!\n\n\n\n\n")
        quit()
    elif info.player.health <= 0:
        print(f"\n\n\n\t\t\t\t\t{info.player.name} lost.\n\n\n\n\n")
        r = input("Would you like to play again?\n> ")
        if r.lower() == "yes":
            reset_player_stats()
            lines_start("")
            classes.get_player_name()
            weapon_pick()
            armor_pick()
            visit_shop()
            arena_enter()
            combat_stats()
            attack_init()
        else:
            quit()

def play_again():
    r = input(f"\nWould {info.player.name} like to continue?\n\n{info.player.name}'s combat stats will reset, but {info.player.name}'s health will not.\n> ")
    if r.lower() != "yes":
        q = input("Are you sure? Type 'q' to quit.\n> ")
        if q.lower() == "q":
            quit()
        else:
            play_again()
    reset_player_stats()
    visit_shop()
    arena_enter()
    combat_stats()
    attack_init()

def reset_player_stats():
    info.player.strength = info.strength_reset
    info.player.defense = info.defense_reset
    info.player.speed = info.speed_reset
    if info.player.health <= 0:
        info.player.health = info.health_reset
        info.opponent.health = info.health_reset

def opponent_drop():
    a = input(f"Would {info.player.name} like to pick up {info.opponent.name}'s dropped items?\n> ")
    if a.lower() == "yes" or a.lower() == "y":
        b = 0
        for items in info.opponent.pouch:
            if info.opponent.pouch[b].amount != 0:
                info.player.pouch[b].amount += info.opponent.pouch[b].amount
                print(f"\n{info.player.name} picked up {info.opponent.pouch[b].amount} {info.opponent.pouch[b].name}.")
            b += 1
        info.player.ls_inventory()
    else:
        c = input("Are you sure? Type 'c' to continue.\n> ")
        if c.lower() == "c":
            return
        else:
            opponent_drop()



explanation()
show_difficulty()
classes.get_player_name()
weapon_pick()
armor_pick()
visit_shop()
arena_enter()
combat_stats()
attack_init()
