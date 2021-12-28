import random
import math
import glad_global_info as info
import glad_classes as classes
import glad_items as items
import glad_inventory as inventory

class Game():
    def __init__(self, pl_low, pl_high, mode_name, num_opponents, stats_low, stats_high, gold_low, gold_high, potion_low, potion_high, swt_low, swt_high, pl_buys_mod, pl_sells_mod):
        self.pl_low = pl_low
        self.pl_high = pl_high
        self.mode_name = mode_name
        self.num_opponents = num_opponents
        self.stats_low = stats_low
        self.stats_high = stats_high
        self.gold_low = gold_low
        self.gold_high = gold_high
        self.potion_low = potion_low
        self.potion_high = potion_high
        self.swt_low = swt_low
        self.swt_high = swt_high
        self.pl_buys_mod = pl_buys_mod
        self.pl_sells_mod = pl_sells_mod

    def gen_pl_stats(self):
        info.player.skill = random.randrange(self.pl_low, self.pl_high)
        info.player.speed = random.randrange(self.pl_low, self.pl_high)
        info.player.strength = random.randrange(self.pl_low, self.pl_high)

    def gen_opponents(self):
        remove_conts = len(info.contestants_ls) - self.num_opponents
        for a in range(remove_conts):
            r = random.randrange(len(info.contestants_ls) - 1)
            del info.contestants_ls [r]


    #: Creates a dictionary from weapon_stats & weapon_names lists.
    #: 2nd dictionary sorts high-low based off of their stats.
    def gen_weapon_containers(self):
        global sorted_weapon_dict
        weapon_stats = []
        weapon_names = []
        b = 0
        for a in enumerate(info.weapon_ls):
            weapon_stats.append((info.weapon_ls[b].speed + info.weapon_ls[b].damage) / 2)
            weapon_names.append(info.weapon_ls[b].name)
            b += 1
        unsorted_weapon_dict = dict((k, v) for k, v in zip(weapon_names, weapon_stats))
        sorted_weapon_dict = sorted(unsorted_weapon_dict.items(), key=lambda x: x[1], reverse=True)

    def gen_weapon(self):
        global weapon_str
        opponent_weapon_pick = random.choices(sorted_weapon_dict, w_odds, k = 1)
        q = (str(opponent_weapon_pick)).split(",")
        weapon_str = q[0].replace("'", "").replace("(", "").replace("[", "")

    #: Find index of picked weapon in info.weapon_ls
    def set_opponent_weapon(self):
        m = 0
        for a in info.weapon_ls:
            if info.weapon_ls[m].name != weapon_str:
                m += 1
            elif info.weapon_ls[m].name == weapon_str:
                info.opponent.weapon = info.weapon_ls[m]


    #: Creates a dictionary from armor_stats & armor_names lists.
    #: 2nd dictionary sorts high-low based off of their stats.
    def gen_armor_containers(self):
        global sorted_armor_dict
        armor_stats = []
        armor_names = []
        b = 0
        for a in enumerate(info.armor_ls):
            armor_stats.append((info.armor_ls[b].defense * 4) - info.armor_ls[b].weight)
            armor_names.append(info.armor_ls[b].name)
            b += 1
        unsorted_armor_dict = dict((k, v) for k, v in zip(armor_names, armor_stats))
        sorted_armor_dict = sorted(unsorted_armor_dict.items(), key=lambda x: x[1], reverse=True)

    #: Best armors and best odds are at the front.
    def gen_armor(self):
        global armor_str
        opponent_armor_pick = random.choices(sorted_armor_dict, a_odds, k = 1)
        q = (str(opponent_armor_pick)).split(",")
        armor_str = q[0].replace("'", "").replace("(", "").replace("[", "")

    #: Find index of picked armor in info.armor_ls
    def set_opponent_armor(self):
        m = 0
        for a in info.armor_ls:
            if info.armor_ls[m].name != armor_str:
                m += 1
            elif info.armor_ls[m].name == armor_str:
                info.opponent.armor = info.armor_ls[m]

    def generate_stats(self):
        count = 0
        for x in info.contestants_ls:
            rand_stat = random.sample(range(self.stats_low, self.stats_high), 3)
            info.contestants_ls[count].skill = rand_stat[0]
            info.contestants_ls[count].speed = rand_stat[1]
            info.contestants_ls[count].strength = rand_stat[2]

            rand_gold = random.randrange(self.gold_low, self.gold_high)
            info.contestants_ls[count].gold.amount = rand_gold

            rand_potion_ls = []
            for y in range(3):
                rand_potion = random.randrange(self.potion_low, self.potion_high)
                rand_potion_ls.append(rand_potion)
            info.contestants_ls[count].strength_potion.amount = rand_potion_ls[0]
            info.contestants_ls[count].defense_potion.amount = rand_potion_ls[1]
            info.contestants_ls[count].speed_potion.amount = rand_potion_ls[2]

            rand_swt = random.randrange(self.swt_low, self.swt_high)
            info.contestants_ls[count].sweetcakes.amount = rand_swt
            count += 1

    def item_quant_check(self, max_potions):
        ls_potions = [info.opponent.strength_potion.amount, info.opponent.speed_potion.amount, info.opponent.defense_potion.amount]
        print(ls_potions)
        potion_index = 0

        def remove_speed_potion():
            if info.opponent.speed_potion.amount > 0:
                info.opponent.speed_potion.amount -= 1
                print(f"Took away a speed potion. {info.opponent.speed_potion.amount}")
        def remove_strength_potion():
            if info.opponent.strength_potion.amount > 0:
                info.opponent.strength_potion.amount -= 1
                print(f"Took away a strength potion. {info.opponent.strength_potion.amount}")
        def remove_defense_potion():
            if info.opponent.defense_potion.amount > 0:
                info.opponent.defense_potion.amount -= 1
                print(f"Took away a defense potion. {info.opponent.defense_potion.amount}")

        def get_total_potions():
            total_potions = 0
            for e in range(len(ls_potions)):
                total_potions += ls_potions[e]
            return total_potions

        potion_disposal = (get_total_potions() - max_potions)
        if potion_disposal > 0:
            print(f"potions to take away: {potion_disposal}")
            for a in range(potion_disposal):
                if potion_disposal > 0:
                    if potion_index == 0:
                        remove_speed_potion()
                        if potion_disposal > 0:
                            remove_strength_potion()
                            if potion_disposal > 0:
                                remove_defense_potion()
                            else:
                                break
                        else:
                            break
                        potion_index = 1
                    elif potion_index == 1:
                        remove_strength_potion()
                        if potion_disposal > 0:
                            remove_defense_potion()
                            if potion_disposal > 0:
                                remove_speed_potion()
                            else:
                                break
                        else:
                            break
                        potion_index = 2
                    elif potion_index == 2:
                        remove_defense_potion()
                        if potion_disposal > 0:
                            remove_speed_potion()
                            if potion_disposal > 0:
                                remove_strength_potion()
                            else:
                                break
                        else:
                            break                                
                        potion_index = 0
                else:
                    break

        print(f"Strength potions: {info.opponent.strength_potion.amount} Defense potions: {info.opponent.defense_potion.amount} Speed potions: {info.opponent.speed_potion.amount}")


class EasyMode(Game):
    def __init__(self):
        super().__init__(6, 9, "Easy", 2, 3, 7, 5, 11, 0, 4, 1, 6, 1, 1)

    def gen_easy_odds(self):
        global w_odds
        global a_odds
        w = len(sorted_weapon_dict)
        a = len(sorted_armor_dict)
        w_odds = []
        a_odds = []
        for b in sorted_weapon_dict:
            w_odds.append(w * 10)
            w += 1
        for b in sorted_armor_dict:
            a_odds.append(a * 10)
            a += 1

class NormalMode(Game):
    def __init__(self):
        super().__init__(5, 11, "Normal", 4, 2, 11, 5, 11, 0, 2, 0, 4, 1.3, 0.8)

    def gen_normal_odds(self):
        global w_odds
        global a_odds
        w = len(sorted_weapon_dict)
        a = len(sorted_armor_dict)
        w_odds = []
        a_odds = []
        for b in sorted_weapon_dict:
            w_odds.append(w * 10)
            w -= 1
        for b in sorted_armor_dict:
            a_odds.append(a * 10)
            a -= 1

class HardMode(Game):
    def __init__(self):
        super().__init__(11, 22, "Hard", 5, 6, 13, 0, 11, 0, 4, 0, 3, 1.5, 0.7)

    def gen_hard_odds(self):
        global w_odds
        global a_odds
        w = len(sorted_weapon_dict)
        a = len(sorted_armor_dict)
        w_odds = []
        a_odds = []
        for b in sorted_weapon_dict:
            w_odds.append(math.exp(w) * 10)
            w -= 1
        for b in sorted_armor_dict:
            a_odds.append(math.exp(a) * 10)
            a -= 1


def find_mode_odds(self):
    if self.mode_name == "Easy":
        self.gen_easy_odds()
        self.item_quant_check(3)
    elif self.mode_name == "Normal":
        self.gen_normal_odds()
        self.item_quant_check(2)
    elif self.mode_name == "Hard":
        self.gen_hard_odds()
        self.item_quant_check(1)
