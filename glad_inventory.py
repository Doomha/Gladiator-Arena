from sys import exit
import glad_items as items
import glad_global_info as info


class Person():
    def __init__(self, name, pl_controlled, gold, potion, sweetcakes):
        self.name = name
        self.gold = items.Gold(gold)
        self.potion = items.Potion(potion)
        self.sweetcakes = items.Sweetcakes(sweetcakes)
        self.pl_controlled = pl_controlled
        self.pouch = [self.gold, self.potion, self.sweetcakes]

    def ls_inventory(self):
        a = 0
        print(f"\n{self.name}'s inventory:")
        print("-" * 10)
        for items in self.pouch:
            if self.pouch[a].amount != 0:
                print(f"{self.pouch[a].name}: {self.pouch[a].amount}")
            a += 1
        print("-" * 10, "\n")

        #: does this thing exist?
    def item_exist(self):
        global item_locator
        item_locator = len(self.pouch) - 1
        item_picked = input("What would you like to consume?\n> ")
        for n in self.pouch:
            if self.pouch[item_locator].name == item_picked.lower():
                break
            elif item_locator == 0:
                print("It looks like that item doesn't exist.")
                return False
            item_locator -= 1

        #: can I consume it?
    def item_consume_check(self):
        if (self.pouch[item_locator].heal) == None and (self.pouch[item_locator].attack_buff) == None and (self.pouch[item_locator].defense_buff) == None and (self.pouch[item_locator].speed_buff) == None:
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
        input(f"{self.name} now has {self.pouch[item_locator].amount} {self.pouch[item_locator].name} left.\n\nPress 'enter' to continue.")



    def person_check(self):
        if self.pl_controlled == False:
            pass
        else:
            pass
