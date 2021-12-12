from sys import exit
import glad_items as items

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
            if self.pouch[a].amount == 0:
                pass
            else:
                print(f"{self.pouch[a].name}: {self.pouch[a].amount}")
            a += 1
        print("-" * 10, "\n")

    def consume_item(self):
        item_picked = input("What would you like to consume?\n> ")
        item_location = len(self.pouch) - 1
        #: does this thing exist?
        for n in self.pouch:
            if self.pouch[item_location].name == item_picked.lower():
                break
            elif item_location == 0:
                print("It looks like that item doesn't exist.")
            item_location -= 1
        #: can I consume it?
        if (self.pouch[item_location].consumable) == False:
            print("This isn't something you can consume.")
            able = False
        else:
            able = True
        #: do I have enough in inventory?
        if able == False:
            pass
        else:
            if self.pouch[item_location].amount == 0:
                print(f"You don't have enough {self.pouch[item_location].name}.")
            else:
                print(f"Good to go! Enjoy your {self.pouch[item_location].name}.")
                print(item_location)
        #: actually consume the item
        if able == False:
            pass
        else:
            self.pouch[item_location].amount -= 1
            print("What a tasty treat!")
            print(f"{self.name} now has {self.pouch[item_location].amount} left.")


    def person_check(self):
        if self.pl_controlled == False:
            pass
        else:
            pass
