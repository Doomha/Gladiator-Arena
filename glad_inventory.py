from sys import exit
import glad_items as items
import glad_global_info as info


class Person():
    def __init__(self, name, pl_controlled, gold, strength_potion, defense_potion, speed_potion, sweetcakes):
        self.name = name
        self.gold = items.Gold(gold)
        self.strength_potion = items.StrengthPotion(strength_potion)
        self.defense_potion = items.DefensePotion(defense_potion)
        self.speed_potion = items.SpeedPotion(speed_potion)
        self.sweetcakes = items.Sweetcakes(sweetcakes)
        self.pl_controlled = pl_controlled
        self.pouch = [self.gold, self.strength_potion, self.defense_potion, self.speed_potion, self.sweetcakes]

    def ls_inventory(self):
        a = 0
        print(f"\n{self.name}'s inventory:")
        print("-" * 10)
        for items in self.pouch:
            if self.pouch[a].name == "gold":
                print(f"{self.pouch[a].name}: {self.pouch[a].amount}")
            elif self.pouch[a].amount != 0:
                print(f"{self.pouch[a].name}: {self.pouch[a].amount}")
            a += 1
        print("-" * 10, "\n")

    def ls_inventory_prices(self):
        a = 0
        print(f"\n{self.name}'s inventory:")
        print("-" * 10)
        for items in self.pouch:
            if self.pouch[a].name == "gold":
                print(f"{self.pouch[a].name}: {self.pouch[a].amount}")
            elif self.pouch[a].amount != 0:
                print(f"{self.pouch[a].name}: {self.pouch[a].amount} - price: {round(self.pouch[a].value * info.game_mode.pl_buys_mod)}")
            a += 1
        print("-" * 10, "\n")

        #: does this thing exist?
    def item_exist(self):
        global item_locator
        item_locator = len(self.pouch) - 1
        p = input(f"What would {info.player.name} like to consume?\n> ")
        item_picked = p.lower()
        for n in self.pouch:
            if self.pouch[item_locator].name == item_picked:
                break
            elif self.pouch[item_locator].name[0: -1] == item_picked:
                break
            elif item_locator == 0:
                print("It looks like that item doesn't exist.")
                return False
            item_locator -= 1

        #: can I consume it?
    def item_consume_check(self):
        w = self.pouch[item_locator]
        if (w.health_incr) == 0 and (w.strength_incr) == 0 and (w.defense_incr) == 0 and (w.speed_incr) == 0:
            print("This isn't something you can consume.")
            return False

        #: do I have enough in inventory?
    def item_inventory_check(self):
            if self.pouch[item_locator].amount == 0:
                print(f"You don't have enough {self.pouch[item_locator].name}.")
                return False

        #: actually consume the item
    def consume_item(self):
        self.pouch[item_locator].amount -= 1
        print(f"\n{self.name} consumed some {self.pouch[item_locator].name}.\n")
        print(f"{self.name} now has {self.pouch[item_locator].amount} {self.pouch[item_locator].name} left.\n")

    def health_increase_check(self):
        if self.pouch[item_locator].health_incr != 0:
            return self.pouch[item_locator].health_incr
        else:
            return False
    def strength_increase_check(self):
        if self.pouch[item_locator].strength_incr != 0:
            return self.pouch[item_locator].strength_incr
        else:
            return False
    def defense_increase_check(self):
        if self.pouch[item_locator].defense_incr != 0:
            return self.pouch[item_locator].defense_incr
        else:
            return False
    def speed_increase_check(self):
        if self.pouch[item_locator].speed_incr != 0:
            return self.pouch[item_locator].speed_incr
        else:
            return False
