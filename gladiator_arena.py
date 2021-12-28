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
        info.game_mode = oppo.NormalMode()
    elif diff_input.lower() == "yes":
        print("Here are the levels of difficulty:\n")
        count = 0
        for a in enumerate(info.game_mode_ls):
            print(info.game_mode_ls[count].mode_name)
            count += 1
        choose_difficulty()
    explain(f"\nYou're playing on {info.game_mode.mode_name} mode.")

def choose_difficulty():
    chosen_diff = input(f"\nType in the level of difficulty you would like to play.\n> ")
    count = 0
    for b in enumerate(info.game_mode_ls):
        if chosen_diff.lower() == info.game_mode_ls[count].mode_name.lower():
            info.game_mode = info.game_mode_ls[count]
        elif count == len(info.game_mode_ls) or chosen_diff == "":
            explain("\nIt looks like you haven't typed in a valid game mode. Try again.")
            choose_difficulty()
        else:
            count += 1

def fight_explain():
    explain("\tWelcome to the fighting pits! Your character will face a series of opponents in a fight to the death. Your goal is to reduce each of your opponent's health to 0. Contestants, including yourself, start with 10 health points.\n")
    explain("\n\tThere are a couple of other stats that will be important to remember...")
    explain("\n\nSkill: The chance one of your attacks hits your opponent. Also helps you dodge your opponent's attacks.")
    explain("\nSpeed: Decides who gets to attack first. Also helps you dodge your opponent's attacks.")
    explain("\nStrength: A key component in calculating the amount of damage your attacks can deal, once they connect with your opponent.\n")
    explain("\n\n\tThat being said, your equipment has an impact on your stats as well. Choose a cumbersome weapon, and your Speed will go down. Attack with something small, and your Strength doesn't do much good.\n")
    explain("\n\n\tOnce in combat, you will be able to choose your fight style, each with their own pros and cons. For example, fighting aggressively improves your speed and strength, while fighting conservatively increases your defense.\n")
    explain("\n\n\tYour character will also be able to buy, sell, and consume items that can boost your stats. Make sure to pace yourself though--your opponents might drop some items, but you'll have to beat them first!\n\n\t\t\t\t\tGood luck!\n\n")
    explain("\n\n\n\n\n")

def pl_stats():
    info.game_mode.gen_pl_stats()
    explain(f"\nHere is {info.player.name}'s skill: {info.player.skill}, speed: {info.player.speed}, strength: {info.player.strength}.\n")
    set_player_stats()

def show_gold():
    lines_start(f"\n{info.player.name} has {info.player.gold.amount} gold. Here are the options {info.player.name} can choose from:")

def visit_smithy():
    a = input(f"\nWould {info.player.name} like to enter the smithy?\n> ")
    if a.lower() != "yes":
        if info.player.weapon == None or info.player.armor == None:
            explain(f"\nIt looks like {info.player.name} isn't properly eqipped yet. Visit the smithy to purchase a weapon and armor.\n")
            smithy_loop()
        else:
            return
    else:
        smithy_loop()

def smithy_exit():
    f = input(f"Is {info.player.name} ready to leave?\n> ")
    if f.lower() == "yes" or f.lower() == "y" or f.lower() == "":
        return
    else:
        smithy_loop()

def smithy_loop():
    if info.player.weapon == None:
        show_gold()
        weapon_pick()
    if info.player.armor == None:
        show_gold()
        armor_pick()
        return
    sell_weapon()
    sell_armor()

def sell_weapon():
    weapon_price = round(info.player.weapon.value * info.game_mode.pl_sells_mod)
    b = input(f"\nWould {info.player.name} like to sell their {info.player.weapon.name} and buy something else?\n> ")
    if b.lower() == "yes" or b.lower() == "y":
        print(f"The smith inspects {info.player.name}'s {info.player.weapon.name}, and is willing to pay {weapon_price} gold for it.")
        c = input(f"Would {info.player.name} like to sell their {info.player.weapon.name}?\n> ")
        if c.lower() == "yes" or b.lower() == "y":
            info.player.gold.amount += weapon_price
            info.player.weapon = None
            show_gold()
            weapon_pick()
            smithy_exit()
            return

def sell_armor():
    armor_price = round(info.player.armor.value * info.game_mode.pl_sells_mod)
    d = input(f"\nWould {info.player.name} like to sell their {info.player.armor.name} and buy something else?\n> ")
    if d.lower() == "yes" or d.lower() == "y":
        print(f"The smith inspects {info.player.name}'s {info.player.armor.name}, and is willing to pay {armor_price} gold for it.")
        e = input(f"Would {info.player.name} like to sell their {info.player.armor.name}?\n> ")
        if e.lower() == "yes" or e.lower() == "y":
            info.player.gold.amount += armor_price
            info.player.armor = None
            show_gold()
            armor_pick()
            smithy_exit()
            return

def weapon_pick():
    def show_weapons():
        for weapon in info.weapon_ls:
            print(f"{weapon.name} -- speed: {weapon.speed} damage: {weapon.damage} cost: {round(weapon.value * info.game_mode.pl_buys_mod)}")
    def weapon_loop():
        count = 0
        weapon_select = input(f"\nWhich weapon would {info.player.name} like to buy?\n> ")
        for weapon in info.weapon_ls:
            if weapon.name.lower() != weapon_select.lower():
                count += 1
            elif weapon.name.lower() == weapon_select.lower():
                if round(weapon.value) <= round(info.player.gold.amount * info.game_mode.pl_buys_mod):
                    info.player.weapon = weapon
                    info.player.gold.amount -= round(weapon.value * info.game_mode.pl_buys_mod)
                    lines_start(f"\n{info.player.name} bought and eqipped a {info.player.weapon.name}. {info.player.name} has {info.player.gold.amount} gold left.")
                    break
                else:
                    explain(f"{info.player.name} needs {round(weapon.value * info.game_mode.pl_buys_mod) - info.player.gold.amount} more gold to be able to afford that weapon. Pick a different one.\n")
                    weapon_loop()
                    break
            if count == len(info.weapon_ls):
                explain("\nIt looks like you haven't typed in a valid weapon option. Try again.")
                weapon_loop()
                break
    show_weapons()
    weapon_loop()

def armor_pick():
    def show_armor():
        for armor in info.armor_ls:
            print(f"{armor.name} -- defense: {armor.defense} weight: {armor.weight} cost: {round(armor.value * info.game_mode.pl_buys_mod)}")
    def armor_loop():
        count = 0
        armor_select = input(f"\nWhich armor would {info.player.name} like to buy?\n> ")
        for armor in info.armor_ls:
            if armor.name.lower() != armor_select.lower():
                count += 1
            elif armor.name.lower() == armor_select.lower():
                if round(armor.value) <= round(info.player.gold.amount * info.game_mode.pl_buys_mod):
                    info.player.armor = armor
                    info.player.gold.amount -= round(armor.value * info.game_mode.pl_buys_mod)
                    lines_start(f"\n{info.player.name} bought and put on {info.player.armor.name}. {info.player.name} has {info.player.gold.amount} gold left.")
                    break
                else:
                    explain(f"{info.player.name} needs {round(armor.value * info.game_mode.pl_buys_mod) - info.player.gold.amount} more gold to be able to afford that armor. Pick a different one.\n")
                    armor_loop()
                    break
            if count == len(info.armor_ls):
                explain("\nIt looks like you haven't typed in a valid armor option. Try again.")
                armor_loop()
                break
    show_armor()
    armor_loop()

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
            print(f"\nIt looks like {info.seller.name} doesn't have that item right now.")
            continue_shopping()
            return False
        info.item_find -= 1

def seller_item_check():
    #: Does seller have the item?
    if info.seller == info.player:
        price_mod = info.game_mode.pl_sells_mod
    elif info.buyer == info.player:
        price_mod = info.game_mode.pl_buys_mod
    if info.seller.pouch[info.item_find].amount == 0:
        explain(f"{info.seller.name} doesn't have enough {info.seller.pouch[info.item_find].name} right now.")
        continue_shopping()
        return False
    elif info.buyer.gold.amount < round(info.seller.pouch[info.item_find].value * price_mod):
        explain(f"{info.buyer.name} doesn't have enough gold right now.")
        continue_shopping()
        return False

def buy_from_seller():
    if info.seller == info.player:
        price_mod = info.game_mode.pl_sells_mod
    elif info.buyer == info.player:
        price_mod = info.game_mode.pl_buys_mod
    bought_item_price = round(info.seller.pouch[info.item_find].value * price_mod)
    info.buyer.gold.amount -= bought_item_price
    info.seller.gold.amount += bought_item_price
    info.buyer.pouch[info.item_find].amount += 1
    info.seller.pouch[info.item_find].amount -= 1
    explain(f"{info.buyer.name} bought 1 {info.buyer.pouch[info.item_find].name} from {info.seller.name} for {bought_item_price} gold.\n")
    continue_shopping()
    return

def continue_shopping():
    c = input(f"\nWould {info.player.name} like to continue shopping?\n> ")
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
            print("\nIt looks like you haven't typed in a valid number. Please try again.\n")
            opponent_input_check()
        else:
            info.valid_opponent_input = int(opponent_input)

    opponent_input_check()
    info.opponent = info.contestants_ls[info.valid_opponent_input - 1]

    def set_opponent_equipment():
        info.game_mode.gen_weapon_containers()
        info.game_mode.gen_armor_containers()
        oppo.find_mode_odds(info.game_mode)
        info.game_mode.gen_weapon()
        info.game_mode.gen_armor()
        info.game_mode.set_opponent_weapon()
        info.game_mode.set_opponent_armor()
    set_opponent_equipment()

    explain(f"\n{info.opponent.name} will be fighting {info.player.name} with a {info.opponent.weapon.name}, which is a {info.opponent.weapon.w_type} weapon. {info.opponent.name} is also equipped with {info.opponent.armor.name}. Good luck!\n")

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
    info.player.get_aggression()
    info.opponent.get_aggression()

    pl_speed_range = (round(info.player.getSpeed() + (info.player.skill) / 2) * 2)
    if pl_speed_range >= info.speed_priority_mod:
        pl_speed_range = info.speed_priority_mod - 1
    opp_speed_range = (round(info.opponent.getSpeed() + (info.opponent.skill) / 2) * 2)
    if opp_speed_range >= info.speed_priority_mod:
        opp_speed_range = info.speed_priority_mod - 1
    true_speed_pl = round(random.randrange(pl_speed_range, info.speed_priority_mod))
    true_speed_opp = round(random.randrange(opp_speed_range, info.speed_priority_mod))

    def attack_priority():
        if true_speed_pl != true_speed_opp:
            if true_speed_pl > true_speed_opp:
                faster = info.player.name
                slower = info.opponent.name
                info.turnCount = info.player
                print(f"\n{faster}'s true speed is {true_speed_pl}, and {slower}'s true speed is {true_speed_opp}.")
            elif true_speed_pl < true_speed_opp:
                faster = info.opponent.name
                slower = info.player.name
                info.turnCount = info.opponent
                print(f"\n{faster}'s true speed is: {true_speed_opp}, and {slower}'s true speed is: {true_speed_pl}.")
            print(f"{faster} gains the upper hand and attacks {slower}.\n")
        elif true_speed_pl == true_speed_opp:
            print(f"\n\nNeither {info.player.name} or {info.opponent.name} is faster. Both of their true speed is {true_speed_pl}.")
            chance = random.randrange(0, 2)
            if chance == 0:
                info.turnCount = info.opponent
                print(f"However, {info.opponent.name} gains the upper hand and attacks.\n")
            elif chance == 1:
                info.turnCount = info.player
                print(f"However, {info.player.name} gains the upper hand and attacks.\n")

    attack_priority()
    attack()


def attack():
    chance = random.randrange(0, info.hit_chance)
    if info.turnCount == info.player:
        source = info.player
        target = info.opponent
    elif info.turnCount == info.opponent:
        source = info.opponent
        target = info.player
    if source.skill + chance >= info.hit_chance:
        explain(f"\n{source.name}'s attack hits!\n")
        damage_done = round(source.getDamage() - (((target.skill + target.speed) * info.attack_evade_mod) + target.defense))

        if damage_done >= 0:
            print(f"{source.name} did {damage_done} damage. {target.name}'s {target.armor.name} blocked {round(target.defense)} damage.")
            target.takeDamage(damage_done)
        else:
            print(f"{source.name} did 1 damage to {target.name}.")
            target.takeDamage(1)
        print(f"{target.name} has {target.health} health left.\n")
        win_condition()
        inventory_loop()
    else:
        explain(f"{source.name}'s attack misses.\n")
    attack_init()

def inventory_loop():
    if prompt_inventory() == True:
        if use_inventory() == True:
            info.player.consume_item()
            trigger_item_effect()
            inventory_loop()

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
        item_explanation("defense", defense_incr, stat) #: This increases the stats of the player's armor, not their defense.

    elif info.player.speed_increase_check() > 0:
        speed_incr = info.player.speed_increase_check()
        info.player.increaseSpeed(speed_incr)
        stat = round(info.player.speed)
        item_explanation("speed", speed_incr, stat)

def win_condition():
    if info.opponent.health <= 0 and (len(info.contestants_ls) - 1) > 0:
        c = info.contestants_ls.index(info.opponent)
        info.contestants_ls.pop(c)
        info.defeated_opponents += 1
        explain(f"\n{info.player.name} beat {info.opponent.name}! {info.player.name} has beaten {info.defeated_opponents} opponents so far.\n")
        info.opponent.ls_inventory()
        opponent_drop()
        play_again()
    elif info.opponent.health <= 0 and (len(info.contestants_ls) - 1) == 0:
        info.defeated_opponents += 1
        print(f"\n\n\t\t\t\t\t{info.player.name} beat {info.opponent.name}! {info.player.name} beat {info.defeated_opponents} opponents in total.")
        lines_end(f"\n\n\t\t\t\t\t{info.player.name} wins!\n\n\n\n\n")
        quit()
    elif info.player.health <= 0:
        print(f"\n\n\n\t\t\t\t\t{info.player.name} lost.\n\n\n\n\n")
        r = input("Would you like to play again?\n> ")
        if r.lower() == "yes":
            main_script()
        else:
            quit()

def play_again():
    r = input(f"\nWould {info.player.name} like to continue?\n\n{info.player.name}'s combat stats will reset, but {info.player.name}'s health ({info.player.health}) will not.\n> ")
    if r.lower() != "yes":
        q = input("Are you sure? Type 'q' to quit.\n> ")
        if q.lower() == "q":
            quit()
        else:
            play_again()
    reset_player_stats()
    visit_smithy()
    visit_shop()
    inventory_loop()
    arena_enter()
    combat_stats()
    attack_init()

def set_player_stats():
    info.health_reset = info.player.health
    info.strength_reset = info.player.strength
    info.defense_reset = info.player.defense
    info.speed_reset = info.player.speed

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


def main_script():
    explanation()
    show_difficulty()
    classes.get_player_name()
    info.game_mode.gen_opponents()
    pl_stats()
    visit_smithy()
    visit_shop()
    info.game_mode.generate_stats()
    arena_enter()
    combat_stats()
    attack_init()

main_script()
